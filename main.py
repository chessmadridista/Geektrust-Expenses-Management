import operations as op
import auxiliary_operations as aux_op

def main():
  commands = aux_op.load_file()
  calculator = aux_op.ExpensesCalculator()
  command_outputs = aux_op.set_command_order_wise(calculator, commands)

  return command_outputs

if __name__ == "__main__":
  print(main())