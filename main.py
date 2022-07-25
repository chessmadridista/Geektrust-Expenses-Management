import operations as op
import auxiliary_operations as aux_op

def main():
  input_commands = op.load_file("LOL")
  command_outputs = self.__set_command_order_wise(input_commands)

  print(command_outputs)

if __name__ == "__main__":
  main()