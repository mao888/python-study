import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # 初始化网络参数
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.bias_output = np.zeros((1, output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, inputs):
        # 前向传播
        self.hidden_sum = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        self.hidden_activation = self.sigmoid(self.hidden_sum)
        self.output_sum = np.dot(self.hidden_activation, self.weights_hidden_output) + self.bias_output
        self.output_activation = self.sigmoid(self.output_sum)
        return self.output_activation

    def backward(self, inputs, targets, learning_rate):
        # 反向传播
        output_error = targets - self.output_activation
        output_delta = output_error * self.sigmoid_derivative(self.output_activation)

        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_activation)

        # 更新权重和偏置
        self.weights_hidden_output += self.hidden_activation.T.dot(output_delta) * learning_rate
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
        self.weights_input_hidden += inputs.T.dot(hidden_delta) * learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

    def train(self, inputs, targets, epochs, learning_rate):
        for epoch in range(epochs):
            for i in range(len(inputs)):
                input_data = np.array([inputs[i]])
                target_data = np.array([targets[i]])
                # 前向传播
                output = self.forward(input_data)
                # 反向传播和参数更新
                self.backward(input_data, target_data, learning_rate)
            # 计算并打印每个epoch的损失
            loss = np.mean(np.square(targets - self.predict(inputs)))
            print(f'Epoch {epoch + 1}/{epochs}, Loss: {loss}')

    def predict(self, inputs):
        # 使用训练后的网络进行预测
        return self.forward(inputs)

# 示例用法
# 定义输入、隐藏层和输出层的神经元数量
input_size = 2
hidden_size = 4
output_size = 1

# 创建神经网络实例
nn = NeuralNetwork(input_size, hidden_size, output_size)

# 训练数据
training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
training_targets = np.array([[0], [1], [1], [0]])

# 训练神经网络
nn.train(training_inputs, training_targets, epochs=10000, learning_rate=0.1)

# 进行预测
new_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
predictions = nn.predict(new_inputs)
print("Predictions:")
print(predictions)
