#!/usr/bin/env python3
"""H17 USB-UART host, stop-and-wait, full byte-for-byte verification. pyserial only for --port."""
import argparse,json,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def crc8(data):
 c=0
 for d in data:
  c^=d
  for _ in range(8):c=((c<<1)^7)&255 if c&128 else (c<<1)&255
 return c
assert crc8(b'123456789')==0xf4

def request(row,seq):
 a,b,m,*_=row
 v=bytes([0xa5,0x5a,1,seq,m])+a.to_bytes(3,'little')+b.to_bytes(3,'little')
 return v+bytes([crc8(v)])
def response(row,seq):
 _,_,_,s,oid,raw,obs,rep=row
 v=bytes([0x5a,0xa5,1,seq,s,oid])+b''.join(x.to_bytes(3,'little') for x in (raw,obs,rep))
 return v+bytes([crc8(v)])
def rows(path):return [list(map(lambda x:int(x,16),line.split())) for line in Path(path).read_text().splitlines() if line.strip()]
def generate():
 v=rows(ROOT/'vectors/quick.txt');cases=[]
 # All modes, valid and non-generating, invalid input/mode; deterministic sample.
 selected=v[:4]+v[105:125]+v[-10:]
 for n,r in enumerate(selected):cases.append((request(r,n),response(r,n)))
 for kind in ['crc','version','wide_mode']:
  p=bytearray(request(v[0],len(cases)))
  if kind=='crc':p[-1]^=1
  elif kind=='version':p[2]=2;p[-1]=crc8(p[:-1])
  else:p[4]=0x80;p[-1]=crc8(p[:-1])
  e=response([0,0,0,5,127,0,0,0],p[3]);cases.append((bytes(p),e))
 # A good request after the bad requests proves parser recovers.
 cases.append((request(v[-2],len(cases)),response(v[-2],len(cases))))
 (ROOT/'vectors/uart.txt').write_text('\n'.join(f'{p.hex()} {q.hex()}' for p,q in cases)+'\n')
 print('UART transactions:',len(cases))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generate',action='store_true');ap.add_argument('--port');ap.add_argument('--vectors',default=str(ROOT/'vectors/demo.txt'));ap.add_argument('--baud',type=int,default=115200);ap.add_argument('--log',default='board_results.jsonl');ap.add_argument('--protocol-tests',action='store_true');a=ap.parse_args()
 if a.generate:generate();return
 if not a.port:ap.error('--port required; e.g. COM5 or /dev/ttyUSB1')
 import serial
 tests=[(request(r,n%256),response(r,n%256)) for n,r in enumerate(rows(a.vectors))]
 if a.protocol_tests:tests=[tuple(bytes.fromhex(x) for x in l.split()) for l in (ROOT/'vectors/uart.txt').read_text().splitlines()]
 with serial.Serial(a.port,a.baud,timeout=1,write_timeout=1) as port,open(a.log,'w') as log:
  time.sleep(.2);port.reset_input_buffer()
  for n,(req,expected) in enumerate(tests):
   t=time.monotonic();port.write(req);port.flush();got=port.read(16);dt=time.monotonic()-t
   ok=got==expected
   log.write(json.dumps(dict(test=n,request=req.hex(),expected=expected.hex(),received=got.hex(),pass_test=ok,host_roundtrip_seconds=dt))+'\n');log.flush()
   if not ok:raise SystemExit(f'FAIL {n}: expected {expected.hex()} got {got.hex()}; reset board and inspect log')
   if n%1000==0:print(n,'PASS')
 print(f'PASS {len(tests)} hardware transactions; log {a.log}')
if __name__=='__main__':main()
