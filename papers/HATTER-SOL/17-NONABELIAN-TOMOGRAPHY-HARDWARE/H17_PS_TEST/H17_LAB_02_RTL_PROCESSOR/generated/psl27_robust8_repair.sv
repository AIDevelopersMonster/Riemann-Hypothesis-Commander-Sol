// Auto-generated H17-06 ROM-free one-erasure repair decoder.
// The erased coordinate is never queried by any decision tree.
module psl27_robust8_repair(
    input  logic [23:0] signature,
    input  logic [2:0]  erased_idx,
    output logic        valid,
    output logic [23:0] repaired_signature
);
always_comb begin
  valid = 1'b0;
  repaired_signature = signature;
  case (erased_idx)
    3'd0: begin // erase AAB: depth=4, nodes=41, states=178, root=ABABB
      case (signature[5:3]) // ABABB
        3'd0: begin
          valid = 1'b0;
        end
        3'd1: begin
          case (signature[14:12]) // Abbb
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              valid = 1'b0;
            end
            3'd2: begin
              case (signature[20:18]) // Abb
                3'd1: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[20:18]) // Abb
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[8:6]) // AAbAb
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd1;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[8:6]) // AAbAb
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd1;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd2: begin
          case (signature[14:12]) // Abbb
            3'd1: begin
              case (signature[20:18]) // Abb
                3'd1: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[20:18]) // Abb
                3'd0: begin
                  valid = 1'b0;
                end
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  case (signature[17:15]) // AAAB
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd3;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd5;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  case (signature[17:15]) // AAAB
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd5: begin
                  case (signature[17:15]) // AAAB
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd2;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[20:18]) // Abb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd2;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd1;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[20:18]) // Abb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd2;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd1;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd3: begin
          case (signature[2:0]) // ABaBB
            3'd1: begin
              case (signature[8:6]) // AAbAb
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  case (signature[17:15]) // AAAB
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd3;
                    end
                    3'd3: begin
                      valid = 1'b0;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd1;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd1;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[20:18]) // Abb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd2;
                end
                3'd2: begin
                  case (signature[17:15]) // AAAB
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd4;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[20:18]) // Abb
                3'd0: begin
                  valid = 1'b0;
                end
                3'd1: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[17:15]) // AAAB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd4;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                3'd3: begin
                  case (signature[14:12]) // Abbb
                    3'd1: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd2;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd2;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd3;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[17:15]) // AAAB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd5;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                3'd3: begin
                  case (signature[14:12]) // Abbb
                    3'd1: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd2;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd2;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd3;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd4: begin
          case (signature[17:15]) // AAAB
            3'd1: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd2;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd4;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[8:6]) // AAbAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd5;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd5;
                end
                3'd5: begin
                  case (signature[20:18]) // Abb
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd2;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd3;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[8:6]) // AAbAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd4;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd5;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[20:18]) // Abb
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd5;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd1;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[20:18]) // Abb
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                3'd4: begin
                  case (signature[14:12]) // Abbb
                    3'd0: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd5;
                    end
                    3'd4: begin
                      valid = 1'b0;
                    end
                    3'd5: begin
                      valid = 1'b0;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd5: begin
          case (signature[17:15]) // AAAB
            3'd1: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd2;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[8:6]) // AAbAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd4;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd1;
                end
                3'd4: begin
                  case (signature[20:18]) // Abb
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd2;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd3;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[8:6]) // AAbAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd5;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[20:18]) // Abb
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd4;
                end
                3'd5: begin
                  case (signature[14:12]) // Abbb
                    3'd0: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[23:21] = 3'd4;
                    end
                    3'd4: begin
                      valid = 1'b0;
                    end
                    3'd5: begin
                      valid = 1'b0;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[20:18]) // Abb
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd4;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd1;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[23:21] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        default: valid = 1'b0;
      endcase
    end
    3'd1: begin // erase Abb: depth=4, nodes=41, states=178, root=AAbAb
      case (signature[8:6]) // AAbAb
        3'd0: begin
          valid = 1'b0;
        end
        3'd1: begin
          case (signature[17:15]) // AAAB
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              valid = 1'b0;
            end
            3'd2: begin
              case (signature[23:21]) // AAB
                3'd1: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[23:21]) // AAB
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[5:3]) // ABABB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd1;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[5:3]) // ABABB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd1;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd2: begin
          case (signature[17:15]) // AAAB
            3'd1: begin
              case (signature[23:21]) // AAB
                3'd1: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[23:21]) // AAB
                3'd0: begin
                  valid = 1'b0;
                end
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  case (signature[14:12]) // Abbb
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd3;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd5;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  case (signature[14:12]) // Abbb
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd5: begin
                  case (signature[14:12]) // Abbb
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[2:0]) // ABaBB
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd2;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[23:21]) // AAB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd2;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd1;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[23:21]) // AAB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd2;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd1;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd3: begin
          case (signature[11:9]) // AABAb
            3'd1: begin
              case (signature[5:3]) // ABABB
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  case (signature[14:12]) // Abbb
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd3;
                    end
                    3'd3: begin
                      valid = 1'b0;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd1;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd1;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[23:21]) // AAB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd2;
                end
                3'd2: begin
                  case (signature[14:12]) // Abbb
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd4;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[23:21]) // AAB
                3'd0: begin
                  valid = 1'b0;
                end
                3'd1: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[14:12]) // Abbb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd4;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                3'd3: begin
                  case (signature[17:15]) // AAAB
                    3'd1: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd2;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd2;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd3;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[14:12]) // Abbb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd5;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                3'd3: begin
                  case (signature[17:15]) // AAAB
                    3'd1: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd2;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd2;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd3;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd4: begin
          case (signature[14:12]) // Abbb
            3'd1: begin
              case (signature[2:0]) // ABaBB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd2;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[5:3]) // ABABB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd5;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd1;
                end
                3'd4: begin
                  case (signature[23:21]) // AAB
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd2;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd3;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[5:3]) // ABABB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd4;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[23:21]) // AAB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd5;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd1;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[23:21]) // AAB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd5;
                end
                3'd5: begin
                  case (signature[17:15]) // AAAB
                    3'd0: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd5;
                    end
                    3'd4: begin
                      valid = 1'b0;
                    end
                    3'd5: begin
                      valid = 1'b0;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd5: begin
          case (signature[14:12]) // Abbb
            3'd1: begin
              case (signature[2:0]) // ABaBB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd2;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd5;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[5:3]) // ABABB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd4;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd4;
                end
                3'd5: begin
                  case (signature[23:21]) // AAB
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd2;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd3;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[5:3]) // ABABB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd5;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd4;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[23:21]) // AAB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                3'd4: begin
                  case (signature[17:15]) // AAAB
                    3'd0: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[20:18] = 3'd4;
                    end
                    3'd4: begin
                      valid = 1'b0;
                    end
                    3'd5: begin
                      valid = 1'b0;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[23:21]) // AAB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd4;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[20:18] = 3'd1;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        default: valid = 1'b0;
      endcase
    end
    3'd2: begin // erase AAAB: depth=4, nodes=43, states=180, root=Abbb
      case (signature[14:12]) // Abbb
        3'd0: begin
          valid = 1'b0;
        end
        3'd1: begin
          case (signature[8:6]) // AAbAb
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              valid = 1'b0;
            end
            3'd2: begin
              valid = 1'b0;
            end
            3'd3: begin
              case (signature[20:18]) // Abb
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[20:18]) // Abb
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[20:18]) // Abb
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd2: begin
          case (signature[23:21]) // AAB
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              valid = 1'b0;
            end
            3'd2: begin
              case (signature[5:3]) // ABABB
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[5:3]) // ABABB
                3'd1: begin
                  case (signature[20:18]) // Abb
                    3'd3: begin
                      valid = 1'b0;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd3;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd3;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                3'd3: begin
                  case (signature[8:6]) // AAbAb
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd2;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd5;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[5:3]) // ABABB
                3'd2: begin
                  case (signature[20:18]) // Abb
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd5;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd3;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                3'd5: begin
                  case (signature[20:18]) // Abb
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd3;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd2;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd4;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[5:3]) // ABABB
                3'd2: begin
                  case (signature[20:18]) // Abb
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd4;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd3;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd1;
                end
                3'd4: begin
                  case (signature[20:18]) // Abb
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd3;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd2;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd4;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd3: begin
          case (signature[20:18]) // Abb
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              case (signature[2:0]) // ABaBB
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[11:9]) // AABAb
                3'd2: begin
                  case (signature[23:21]) // AAB
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd2;
                    end
                    3'd3: begin
                      valid = 1'b0;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd4;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  case (signature[5:3]) // ABABB
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd2;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd3;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd1;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd5: begin
                  case (signature[5:3]) // ABABB
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd2;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd3;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd1;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[8:6]) // AAbAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd2;
                end
                3'd2: begin
                  case (signature[23:21]) // AAB
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd2;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd5;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  case (signature[11:9]) // AABAb
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b0;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd3;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd3;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[23:21]) // AAB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd5;
                end
                3'd2: begin
                  case (signature[11:9]) // AABAb
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd2;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[23:21]) // AAB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd4;
                end
                3'd2: begin
                  case (signature[11:9]) // AABAb
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd2;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd4: begin
          case (signature[23:21]) // AAB
            3'd1: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd2;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[5:3]) // ABABB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd4;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd1;
                end
                3'd5: begin
                  valid = 1'b0;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[5:3]) // ABABB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[20:18]) // Abb
                3'd0: begin
                  valid = 1'b0;
                end
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd1;
                end
                3'd4: begin
                  case (signature[11:9]) // AABAb
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd3;
                    end
                    3'd4: begin
                      valid = 1'b0;
                    end
                    3'd5: begin
                      valid = 1'b0;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd5: begin
                  valid = 1'b0;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd1;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd5: begin
          case (signature[23:21]) // AAB
            3'd1: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd2;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd5;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[5:3]) // ABABB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd5;
                end
                3'd4: begin
                  valid = 1'b0;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd1;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[5:3]) // ABABB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[20:18]) // Abb
                3'd0: begin
                  valid = 1'b0;
                end
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[17:15] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b0;
                end
                3'd5: begin
                  case (signature[11:9]) // AABAb
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[17:15] = 3'd3;
                    end
                    3'd4: begin
                      valid = 1'b0;
                    end
                    3'd5: begin
                      valid = 1'b0;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        default: valid = 1'b0;
      endcase
    end
    3'd3: begin // erase Abbb: depth=4, nodes=43, states=180, root=AAAB
      case (signature[17:15]) // AAAB
        3'd0: begin
          valid = 1'b0;
        end
        3'd1: begin
          case (signature[5:3]) // ABABB
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              valid = 1'b0;
            end
            3'd2: begin
              valid = 1'b0;
            end
            3'd3: begin
              case (signature[23:21]) // AAB
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[23:21]) // AAB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[23:21]) // AAB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd2: begin
          case (signature[20:18]) // Abb
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              valid = 1'b0;
            end
            3'd2: begin
              case (signature[8:6]) // AAbAb
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[8:6]) // AAbAb
                3'd1: begin
                  case (signature[23:21]) // AAB
                    3'd3: begin
                      valid = 1'b0;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd3;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd3;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                3'd3: begin
                  case (signature[5:3]) // ABABB
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd2;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd4;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[8:6]) // AAbAb
                3'd2: begin
                  case (signature[23:21]) // AAB
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd5;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd3;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                3'd5: begin
                  case (signature[23:21]) // AAB
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd3;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd2;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd5;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[8:6]) // AAbAb
                3'd2: begin
                  case (signature[23:21]) // AAB
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd4;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd3;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd1;
                end
                3'd4: begin
                  case (signature[23:21]) // AAB
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd3;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd2;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd5;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd3: begin
          case (signature[23:21]) // AAB
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  case (signature[20:18]) // Abb
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd2;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd4;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  case (signature[8:6]) // AAbAb
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd2;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd3;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd1;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd5: begin
                  case (signature[8:6]) // AAbAb
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd2;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd3;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd1;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[5:3]) // ABABB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd2;
                end
                3'd2: begin
                  case (signature[20:18]) // Abb
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd2;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd5;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  case (signature[11:9]) // AABAb
                    3'd0: begin
                      valid = 1'b0;
                    end
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd3;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd3;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[20:18]) // Abb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd4;
                end
                3'd2: begin
                  case (signature[11:9]) // AABAb
                    3'd1: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd5;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd2;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[20:18]) // Abb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd5;
                end
                3'd2: begin
                  case (signature[11:9]) // AABAb
                    3'd1: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd4;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd2;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd4: begin
          case (signature[20:18]) // Abb
            3'd1: begin
              case (signature[8:6]) // AAbAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[8:6]) // AAbAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd5;
                end
                3'd4: begin
                  valid = 1'b0;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd1;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd2;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd1;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[23:21]) // AAB
                3'd0: begin
                  valid = 1'b0;
                end
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd1;
                end
                3'd4: begin
                  case (signature[11:9]) // AABAb
                    3'd0: begin
                      valid = 1'b0;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd3;
                    end
                    3'd4: begin
                      valid = 1'b0;
                    end
                    3'd5: begin
                      valid = 1'b0;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd5: begin
                  valid = 1'b0;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd5: begin
          case (signature[20:18]) // Abb
            3'd1: begin
              case (signature[8:6]) // AAbAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd4;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[8:6]) // AAbAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd4;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd1;
                end
                3'd5: begin
                  valid = 1'b0;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd2;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[23:21]) // AAB
                3'd0: begin
                  valid = 1'b0;
                end
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b0;
                end
                3'd5: begin
                  case (signature[11:9]) // AABAb
                    3'd0: begin
                      valid = 1'b0;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[14:12] = 3'd3;
                    end
                    3'd4: begin
                      valid = 1'b0;
                    end
                    3'd5: begin
                      valid = 1'b0;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd1;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[14:12] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        default: valid = 1'b0;
      endcase
    end
    3'd4: begin // erase AABAb: depth=4, nodes=30, states=178, root=ABaBB
      case (signature[2:0]) // ABaBB
        3'd0: begin
          valid = 1'b0;
        end
        3'd1: begin
          case (signature[23:21]) // AAB
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              case (signature[17:15]) // AAAB
                3'd0: begin
                  valid = 1'b0;
                end
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  case (signature[20:18]) // Abb
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[11:9] = 3'd1;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[17:15]) // AAAB
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[20:18]) // Abb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd1;
                end
                3'd2: begin
                  case (signature[17:15]) // AAAB
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b0;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[11:9] = 3'd2;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[11:9] = 3'd2;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[20:18]) // Abb
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd3;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd1;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd1;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[20:18]) // Abb
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd3;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd1;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd1;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd2: begin
          case (signature[20:18]) // Abb
            3'd1: begin
              case (signature[17:15]) // AAAB
                3'd1: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              valid = 1'b1;
              repaired_signature[11:9] = 3'd2;
            end
            3'd3: begin
              case (signature[8:6]) // AAbAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd1;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd2;
                end
                3'd3: begin
                  case (signature[14:12]) // Abbb
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[11:9] = 3'd1;
                    end
                    3'd3: begin
                      valid = 1'b0;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[11:9] = 3'd1;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[11:9] = 3'd1;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              valid = 1'b1;
              repaired_signature[11:9] = 3'd2;
            end
            3'd5: begin
              valid = 1'b1;
              repaired_signature[11:9] = 3'd2;
            end
            default: valid = 1'b0;
          endcase
        end
        3'd3: begin
          case (signature[5:3]) // ABABB
            3'd1: begin
              case (signature[14:12]) // Abbb
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              valid = 1'b1;
              repaired_signature[11:9] = 3'd1;
            end
            3'd3: begin
              case (signature[23:21]) // AAB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd1;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              valid = 1'b1;
              repaired_signature[11:9] = 3'd4;
            end
            3'd5: begin
              valid = 1'b1;
              repaired_signature[11:9] = 3'd5;
            end
            default: valid = 1'b0;
          endcase
        end
        3'd4: begin
          case (signature[14:12]) // Abbb
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              valid = 1'b1;
              repaired_signature[11:9] = 3'd4;
            end
            3'd2: begin
              case (signature[5:3]) // ABABB
                3'd2: begin
                  case (signature[23:21]) // AAB
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[11:9] = 3'd5;
                    end
                    3'd4: begin
                      valid = 1'b0;
                    end
                    3'd5: begin
                      valid = 1'b0;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd5;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[20:18]) // Abb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd3;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[23:21]) // AAB
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b0;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd1;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[23:21]) // AAB
                3'd2: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd4;
                end
                3'd5: begin
                  case (signature[20:18]) // Abb
                    3'd1: begin
                      valid = 1'b1;
                      repaired_signature[11:9] = 3'd3;
                    end
                    3'd4: begin
                      valid = 1'b0;
                    end
                    3'd5: begin
                      valid = 1'b0;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd5: begin
          case (signature[14:12]) // Abbb
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              valid = 1'b1;
              repaired_signature[11:9] = 3'd5;
            end
            3'd2: begin
              case (signature[5:3]) // ABABB
                3'd2: begin
                  case (signature[23:21]) // AAB
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[11:9] = 3'd4;
                    end
                    3'd4: begin
                      valid = 1'b0;
                    end
                    3'd5: begin
                      valid = 1'b0;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd4;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[20:18]) // Abb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd3;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[23:21]) // AAB
                3'd2: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  case (signature[20:18]) // Abb
                    3'd1: begin
                      valid = 1'b1;
                      repaired_signature[11:9] = 3'd3;
                    end
                    3'd4: begin
                      valid = 1'b0;
                    end
                    3'd5: begin
                      valid = 1'b0;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[23:21]) // AAB
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[11:9] = 3'd1;
                end
                3'd5: begin
                  valid = 1'b0;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        default: valid = 1'b0;
      endcase
    end
    3'd5: begin // erase AAbAb: depth=4, nodes=39, states=180, root=Abb
      case (signature[20:18]) // Abb
        3'd0: begin
          valid = 1'b0;
        end
        3'd1: begin
          case (signature[17:15]) // AAAB
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              valid = 1'b0;
            end
            3'd2: begin
              valid = 1'b0;
            end
            3'd3: begin
              case (signature[23:21]) // AAB
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[14:12]) // Abbb
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[14:12]) // Abbb
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd2: begin
          case (signature[17:15]) // AAAB
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[14:12]) // Abbb
                3'd0: begin
                  valid = 1'b0;
                end
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  case (signature[5:3]) // ABABB
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd3;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd5;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b0;
                end
                3'd5: begin
                  valid = 1'b0;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[23:21]) // AAB
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  case (signature[5:3]) // ABABB
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd2;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd4;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  case (signature[14:12]) // Abbb
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd2;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[14:12]) // Abbb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd5;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[14:12]) // Abbb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd4;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd3: begin
          case (signature[14:12]) // Abbb
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[5:3]) // ABABB
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                3'd3: begin
                  case (signature[11:9]) // AABAb
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd3;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd3;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[17:15]) // AAAB
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  case (signature[23:21]) // AAB
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd2;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd1;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd1;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  case (signature[23:21]) // AAB
                    3'd0: begin
                      valid = 1'b0;
                    end
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd3;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                3'd2: begin
                  case (signature[23:21]) // AAB
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd5;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd2;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                3'd2: begin
                  case (signature[23:21]) // AAB
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd4;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd2;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd4: begin
          case (signature[5:3]) // ABABB
            3'd1: begin
              case (signature[23:21]) // AAB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd5;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[23:21]) // AAB
                3'd2: begin
                  case (signature[14:12]) // Abbb
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd5;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd4;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[14:12]) // Abbb
                3'd0: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b0;
                end
                3'd5: begin
                  valid = 1'b0;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[17:15]) // AAAB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd1;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd5: begin
          case (signature[5:3]) // ABABB
            3'd1: begin
              case (signature[23:21]) // AAB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd4;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[23:21]) // AAB
                3'd2: begin
                  case (signature[14:12]) // Abbb
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[8:6] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd4;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd5;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[17:15]) // AAAB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd1;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[14:12]) // Abbb
                3'd0: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[8:6] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b0;
                end
                3'd5: begin
                  valid = 1'b0;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        default: valid = 1'b0;
      endcase
    end
    3'd6: begin // erase ABABB: depth=4, nodes=39, states=180, root=AAB
      case (signature[23:21]) // AAB
        3'd0: begin
          valid = 1'b0;
        end
        3'd1: begin
          case (signature[14:12]) // Abbb
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              valid = 1'b0;
            end
            3'd2: begin
              valid = 1'b0;
            end
            3'd3: begin
              case (signature[20:18]) // Abb
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[17:15]) // AAAB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[17:15]) // AAAB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd2: begin
          case (signature[14:12]) // Abbb
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              case (signature[8:6]) // AAbAb
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[17:15]) // AAAB
                3'd0: begin
                  valid = 1'b0;
                end
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  case (signature[8:6]) // AAbAb
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd3;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd4;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b0;
                end
                3'd5: begin
                  valid = 1'b0;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[20:18]) // Abb
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  case (signature[8:6]) // AAbAb
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd2;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd5;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  case (signature[17:15]) // AAAB
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd2;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[17:15]) // AAAB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd4;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[17:15]) // AAAB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd5;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd3: begin
          case (signature[17:15]) // AAAB
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  case (signature[8:6]) // AAbAb
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd3;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd5;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[14:12]) // Abbb
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  case (signature[20:18]) // Abb
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd2;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd1;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd1;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  case (signature[20:18]) // Abb
                    3'd0: begin
                      valid = 1'b0;
                    end
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd3;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[8:6]) // AAbAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                3'd2: begin
                  case (signature[11:9]) // AABAb
                    3'd1: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd4;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[8:6]) // AAbAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                3'd2: begin
                  case (signature[11:9]) // AABAb
                    3'd1: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd5;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd4: begin
          case (signature[8:6]) // AAbAb
            3'd1: begin
              case (signature[20:18]) // Abb
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd5;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[20:18]) // Abb
                3'd2: begin
                  case (signature[17:15]) // AAAB
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd5;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[17:15]) // AAAB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd1;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[17:15]) // AAAB
                3'd0: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b0;
                end
                3'd5: begin
                  valid = 1'b0;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd5: begin
          case (signature[8:6]) // AAbAb
            3'd1: begin
              case (signature[20:18]) // Abb
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd4;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[20:18]) // Abb
                3'd2: begin
                  case (signature[17:15]) // AAAB
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[5:3] = 3'd4;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd4;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[11:9]) // AABAb
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd5;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[17:15]) // AAAB
                3'd0: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b0;
                end
                3'd5: begin
                  valid = 1'b0;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[17:15]) // AAAB
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd1;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd3;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[5:3] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        default: valid = 1'b0;
      endcase
    end
    3'd7: begin // erase ABaBB: depth=4, nodes=30, states=178, root=AABAb
      case (signature[11:9]) // AABAb
        3'd0: begin
          valid = 1'b0;
        end
        3'd1: begin
          case (signature[23:21]) // AAB
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              case (signature[20:18]) // Abb
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd1;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              case (signature[17:15]) // AAAB
                3'd1: begin
                  case (signature[14:12]) // Abbb
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b0;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[2:0] = 3'd2;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[2:0] = 3'd2;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[5:3]) // ABABB
                3'd1: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd3;
                end
                3'd3: begin
                  case (signature[17:15]) // AAAB
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b0;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[2:0] = 3'd1;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[2:0] = 3'd1;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[20:18]) // Abb
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd1;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd1;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[20:18]) // Abb
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd2;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd1;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd1;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd2: begin
          case (signature[23:21]) // AAB
            3'd1: begin
              case (signature[17:15]) // AAAB
                3'd1: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              valid = 1'b1;
              repaired_signature[2:0] = 3'd2;
            end
            3'd3: begin
              case (signature[5:3]) // ABABB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd1;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd2;
                end
                3'd3: begin
                  case (signature[17:15]) // AAAB
                    3'd1: begin
                      valid = 1'b0;
                    end
                    3'd2: begin
                      valid = 1'b1;
                      repaired_signature[2:0] = 3'd1;
                    end
                    3'd3: begin
                      valid = 1'b0;
                    end
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[2:0] = 3'd1;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[2:0] = 3'd1;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd2;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd2;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              valid = 1'b1;
              repaired_signature[2:0] = 3'd2;
            end
            3'd5: begin
              valid = 1'b1;
              repaired_signature[2:0] = 3'd2;
            end
            default: valid = 1'b0;
          endcase
        end
        3'd3: begin
          case (signature[8:6]) // AAbAb
            3'd1: begin
              case (signature[17:15]) // AAAB
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd5;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd2: begin
              valid = 1'b1;
              repaired_signature[2:0] = 3'd1;
            end
            3'd3: begin
              case (signature[23:21]) // AAB
                3'd0: begin
                  valid = 1'b0;
                end
                3'd1: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd1;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd1;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              valid = 1'b1;
              repaired_signature[2:0] = 3'd5;
            end
            3'd5: begin
              valid = 1'b1;
              repaired_signature[2:0] = 3'd4;
            end
            default: valid = 1'b0;
          endcase
        end
        3'd4: begin
          case (signature[14:12]) // Abbb
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              valid = 1'b1;
              repaired_signature[2:0] = 3'd4;
            end
            3'd2: begin
              case (signature[5:3]) // ABABB
                3'd2: begin
                  case (signature[23:21]) // AAB
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[2:0] = 3'd5;
                    end
                    3'd4: begin
                      valid = 1'b0;
                    end
                    3'd5: begin
                      valid = 1'b0;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd5;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd5;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[17:15]) // AAAB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd5;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd5;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd5;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd3;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd1;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[20:18]) // Abb
                3'd0: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b0;
                end
                3'd5: begin
                  valid = 1'b0;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[23:21]) // AAB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd3;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  case (signature[20:18]) // Abb
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[2:0] = 3'd4;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[2:0] = 3'd3;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd5: begin
                  valid = 1'b0;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        3'd5: begin
          case (signature[14:12]) // Abbb
            3'd0: begin
              valid = 1'b0;
            end
            3'd1: begin
              valid = 1'b1;
              repaired_signature[2:0] = 3'd5;
            end
            3'd2: begin
              case (signature[5:3]) // ABABB
                3'd2: begin
                  case (signature[23:21]) // AAB
                    3'd2: begin
                      valid = 1'b0;
                    end
                    3'd3: begin
                      valid = 1'b1;
                      repaired_signature[2:0] = 3'd4;
                    end
                    3'd4: begin
                      valid = 1'b0;
                    end
                    3'd5: begin
                      valid = 1'b0;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd4;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd4;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd3: begin
              case (signature[17:15]) // AAAB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd4;
                end
                3'd2: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd4;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd4;
                end
                3'd4: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd1;
                end
                3'd5: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd3;
                end
                default: valid = 1'b0;
              endcase
            end
            3'd4: begin
              case (signature[23:21]) // AAB
                3'd1: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd3;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd4: begin
                  valid = 1'b0;
                end
                3'd5: begin
                  case (signature[20:18]) // Abb
                    3'd4: begin
                      valid = 1'b1;
                      repaired_signature[2:0] = 3'd3;
                    end
                    3'd5: begin
                      valid = 1'b1;
                      repaired_signature[2:0] = 3'd5;
                    end
                    default: valid = 1'b0;
                  endcase
                end
                default: valid = 1'b0;
              endcase
            end
            3'd5: begin
              case (signature[20:18]) // Abb
                3'd0: begin
                  valid = 1'b0;
                end
                3'd2: begin
                  valid = 1'b0;
                end
                3'd3: begin
                  valid = 1'b1;
                  repaired_signature[2:0] = 3'd1;
                end
                3'd4: begin
                  valid = 1'b0;
                end
                3'd5: begin
                  valid = 1'b0;
                end
                default: valid = 1'b0;
              endcase
            end
            default: valid = 1'b0;
          endcase
        end
        default: valid = 1'b0;
      endcase
    end
    default: begin valid = 1'b0; repaired_signature = signature; end
  endcase
end
endmodule
