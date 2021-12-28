import matplotlib.pyplot as plt

x_list = ["1,000", "10,000", "100,000", "1,000,000"]
save_python_list = [0.015622138977050781, 0.031280517578125, 0.45635390281677246, 3.636035442352295]
load_python_list = [0.0, 0.0, 0.08066201210021973, 0.8806850910186768]
plot_python_list = [0.9582583904266357, 8.063527822494507, 79.8804624080658, 855.8578388690948]
save_java_list = [0.125, 0.083, 0.39, 4.114]
load_java_list = [0.047, 0.094, 0.375, 3.116]
plot_java_list = [0.7, 0.7, 1.1, 9]

plt.subplot(311)
plt.title("Python - blue          Java - green")
plt.plot(x_list, save_python_list, "bo-", label="python")
plt.plot(x_list, save_java_list, "go-", label="java")
plt.ylabel("time to save")
plt.subplot(312)
plt.plot(x_list, load_python_list, "bo-", label="python load")
plt.plot(x_list, load_java_list, "go-", label="java load")
plt.ylabel("time to load")
plt.subplot(313)
plt.plot(x_list, plot_python_list, "bo-")
plt.plot(x_list, plot_java_list, "go-")
plt.xlabel("graph size")
plt.ylabel("time to plot")

plt.show()
