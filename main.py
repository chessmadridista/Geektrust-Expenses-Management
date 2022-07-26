import operations as op
import auxiliary_operations as aux_op

def main():
  commands = aux_op.load_file()
  calculator = aux_op.ExpensesCalculator()
  command_outputs = calculator.set_command_order_wise(commands)

  return command_outputs

if __name__ == "__main__":
  print(main())