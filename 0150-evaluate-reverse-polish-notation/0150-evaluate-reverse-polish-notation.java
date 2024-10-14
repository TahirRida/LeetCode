class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> ops = new Stack<>();

        for (int i = 0; i < tokens.length; i++) {
            switch (tokens[i]) {
                case "+":
                    ops.push(ops.pop() + ops.pop());
                    break;
                case "-":
                    int subtrahend = ops.pop(); // second operand
                    int minuend = ops.pop(); // first operand
                    ops.push(minuend - subtrahend);
                    break;
                case "*":
                    ops.push(ops.pop() * ops.pop());
                    break;
                case "/":
                    int divisor = ops.pop(); // second operand
                    int dividend = ops.pop(); // first operand
                    ops.push(dividend / divisor);
                    break;
                default:
                    ops.push(Integer.parseInt(tokens[i]));
                    break;
            }
        }
        return ops.pop();
    }
}
