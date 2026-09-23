# H19-LAB-02 · Gowin GW5A-25A provenance SHA-256 manifest

Status: GENERATED FROM LOCAL PHYSICAL RUN ARTIFACTS

Manifest-generation branch: research/hatter-sol-19-boolean-geometry
Manifest-generation HEAD: d30356302fcc533d857ced8cad4daa84c5a29ffe
Target: GW5A-25A / GW5A-LV25MG121NC1/I0
Tool flow: Gowin Education IDE 1.9.9Beta-4 / gw_sh
Clock contract: clk = 100 MHz, SDC period 10.000 ns
Dual-purpose I/O configuration used for physical fit: MSPI + READY as GPIO
Hash: SHA-256

The heavy generated/ and gowin_1_9_9b4_pnr/ directories are intentionally not tracked.
This manifest fingerprints the generated RTL, explicit SDC/Tcl inputs, saved Gowin option snapshots, primary transcripts, synthesis reports, P&R resource reports, and post-route timing reports used by the frozen H19-LAB-02 result.

| mode | kind | bytes | SHA-256 | relative path |
| --- | --- | ---: | --- | --- |
| direct12 | generated-rtl | 2071 | 82a6e768acf9cf2e2aa248993103caa35ec2111f4a657896c5e534478bc586c6 | generated\direct12\psl27_membership_only.sv |
| direct12 | generated-rtl | 2382 | 5cd3d19df66b9310ef955b9f6bb510872fea1782caf31aef9deca3c5a08ebb15 | generated\direct12\psl27_member_class_only.sv |
| direct12 | generated-rtl | 91413 | e559a38763ab6942aa8ad3b505855a5000a69ce2699a5689661e930b441eebdd | generated\direct12\h18_r12_comb_core.sv |
| direct12 | generated-rtl | 2011 | 4bb22bb5e607fa058844755a4812ce52a19d0d648ca1559989a220d6bedd9e93 | generated\direct12\h18_r12_comb_controller.sv |
| direct12 | gowin-input | 57 | 3706f2f5fe329dc9354939bd1b8df11913846c146f2f75b66d5831ccc601c38f | gowin_1_9_9b4_pnr\direct12\h19_direct12_gw5a25_pnr.sdc |
| direct12 | gowin-input | 1537 | 705814251dfe76c863c98f1d5635f6082135e193d8deb5a7f008f533bd937529 | gowin_1_9_9b4_pnr\direct12\h19_direct12_gw5a25_pnr.tcl |
| direct12 | gowin-snapshot | 3737 | f2f00cecc02c5b0b6159c9f5746d72a50b332388272977162f9402e832e8d4fa | gowin_1_9_9b4_pnr\direct12\h19_direct12_gw5a25_pnr_snapshot.tcl |
| direct12 | gowin-transcript | 7389 | 9cf18509d5e54c38fc9ed80b07beec991cdc86b5aa045aa2bd4607ee0c8c3a69 | gowin_1_9_9b4_pnr\direct12\h19_direct12_gw5a25_pnr.log |
| direct12 | gowin-synthesis-report | 91054 | 6a07d01c31ea6bbe09dc6dd0f92ed15487b4fcca3ebb3327639fe49af16cf8b9 | gowin_1_9_9b4_pnr\direct12\impl\gwsynthesis\h19_direct12_gw5a25_pnr_syn.rpt.html |
| direct12 | gowin-pnr-report | 39190 | 214e961443a7c5890358e53820eae3f7e52b2f7f8b4d2e15390d74bb5b6911ab | gowin_1_9_9b4_pnr\direct12\impl\pnr\h19_direct12_gw5a25_pnr.rpt.txt |
| direct12 | gowin-timing-report | 254293 | 1a68090d3802f35a85c53c82a08edd7be340a1ad542a9f675ddbe8a68ba8795d | gowin_1_9_9b4_pnr\direct12\impl\pnr\h19_direct12_gw5a25_pnr.tr |
| prefix19 | generated-rtl | 2071 | 82a6e768acf9cf2e2aa248993103caa35ec2111f4a657896c5e534478bc586c6 | generated\prefix19\psl27_membership_only.sv |
| prefix19 | generated-rtl | 2382 | 5cd3d19df66b9310ef955b9f6bb510872fea1782caf31aef9deca3c5a08ebb15 | generated\prefix19\psl27_member_class_only.sv |
| prefix19 | generated-rtl | 91230 | c92937efc86f0c97fec68028f23020b96da716044a232f95e61609290082264c | generated\prefix19\h18_r12_comb_core.sv |
| prefix19 | generated-rtl | 2011 | 4bb22bb5e607fa058844755a4812ce52a19d0d648ca1559989a220d6bedd9e93 | generated\prefix19\h18_r12_comb_controller.sv |
| prefix19 | gowin-input | 57 | 3706f2f5fe329dc9354939bd1b8df11913846c146f2f75b66d5831ccc601c38f | gowin_1_9_9b4_pnr\prefix19\h19_prefix19_gw5a25_pnr.sdc |
| prefix19 | gowin-input | 1537 | 87c5ba7cf5f4c895c66856b51b64cf4260c9be698f3497d361b500da024fe3cd | gowin_1_9_9b4_pnr\prefix19\h19_prefix19_gw5a25_pnr.tcl |
| prefix19 | gowin-snapshot | 3737 | 00e1b4c3cd1991bbb548655c6a156ce220be8de00e02b20f4aba176a847da7ba | gowin_1_9_9b4_pnr\prefix19\h19_prefix19_gw5a25_pnr_snapshot.tcl |
| prefix19 | gowin-transcript | 7389 | 0704fc15a1046a9e3a3afe352e4a9e3e041d5e6f273c2e62f46d5a2c166bf817 | gowin_1_9_9b4_pnr\prefix19\h19_prefix19_gw5a25_pnr.log |
| prefix19 | gowin-synthesis-report | 91054 | 6be167024957bb87f34fef7d88aefefcc975e895707f9fde32fc5b63d6a99a22 | gowin_1_9_9b4_pnr\prefix19\impl\gwsynthesis\h19_prefix19_gw5a25_pnr_syn.rpt.html |
| prefix19 | gowin-pnr-report | 39190 | 907957fb98ba0309fbae3571f884ee28e6917470e7b7a89caa19ec8cc9d0116e | gowin_1_9_9b4_pnr\prefix19\impl\pnr\h19_prefix19_gw5a25_pnr.rpt.txt |
| prefix19 | gowin-timing-report | 254293 | de80e5f1dbfe7dcd4e56a9077a4d74b45d80fa44bbe4151472f2ebe184007104 | gowin_1_9_9b4_pnr\prefix19\impl\pnr\h19_prefix19_gw5a25_pnr.tr |
| nielsen12 | generated-rtl | 2071 | 82a6e768acf9cf2e2aa248993103caa35ec2111f4a657896c5e534478bc586c6 | generated\nielsen12\psl27_membership_only.sv |
| nielsen12 | generated-rtl | 2382 | 5cd3d19df66b9310ef955b9f6bb510872fea1782caf31aef9deca3c5a08ebb15 | generated\nielsen12\psl27_member_class_only.sv |
| nielsen12 | generated-rtl | 92322 | 90d5129164d0407584ce1776fb8d9966a4d6fe1ae184dcf936959d9e3b57adfd | generated\nielsen12\h18_r12_comb_core.sv |
| nielsen12 | generated-rtl | 2011 | 4bb22bb5e607fa058844755a4812ce52a19d0d648ca1559989a220d6bedd9e93 | generated\nielsen12\h18_r12_comb_controller.sv |
| nielsen12 | gowin-input | 57 | 3706f2f5fe329dc9354939bd1b8df11913846c146f2f75b66d5831ccc601c38f | gowin_1_9_9b4_pnr\nielsen12\h19_nielsen12_gw5a25_pnr.sdc |
| nielsen12 | gowin-input | 1546 | 8573094d9bec586490f5c36b2e914888cd755893906ed1d7c40484a0196dc482 | gowin_1_9_9b4_pnr\nielsen12\h19_nielsen12_gw5a25_pnr.tcl |
| nielsen12 | gowin-snapshot | 3744 | e74b9df3446c428cb8561256c8c0f20ac2d7e62db4e41b7089c993f0465c1956 | gowin_1_9_9b4_pnr\nielsen12\h19_nielsen12_gw5a25_pnr_snapshot.tcl |
| nielsen12 | gowin-transcript | 7425 | 9ee08f753df668ae3662e09085de948100c74a0ff985df1c96acb9583970d8e3 | gowin_1_9_9b4_pnr\nielsen12\h19_nielsen12_gw5a25_pnr.log |
| nielsen12 | gowin-synthesis-report | 90692 | daef8509542a1703b5a7225a1a797b2e3a3d3382e858a8f410978ab64914d70a | gowin_1_9_9b4_pnr\nielsen12\impl\gwsynthesis\h19_nielsen12_gw5a25_pnr_syn.rpt.html |
| nielsen12 | gowin-pnr-report | 39194 | 09a81219267dd28d440065b16b4befb0d8b479de0f70ef00894c11249f8b77b5 | gowin_1_9_9b4_pnr\nielsen12\impl\pnr\h19_nielsen12_gw5a25_pnr.rpt.txt |
| nielsen12 | gowin-timing-report | 245032 | 41edfed1e2a9163a75f88d6c7ce1c3ce1c52a481391f05ad367a9db94bbaa8cd | gowin_1_9_9b4_pnr\nielsen12\impl\pnr\h19_nielsen12_gw5a25_pnr.tr |

Files fingerprinted: 33

Claim boundary: hashes certify these local files byte-for-byte. They do not prove deterministic placement/routing across machines, tool installations, seeds, or future Gowin versions.
