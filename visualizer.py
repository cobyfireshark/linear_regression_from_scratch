# visualizer.py
import matplotlib.pyplot as plt

def plot_xy_data(data, figure_path):
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1])
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('Scatter Plot of Data')
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.savefig(figure_path)
    plt.close()

def plot_lines(x_values, linear_definitions, figure_path):
    for (slope, y_intercept) in linear_definitions:
        y_values = slope * x_values + y_intercept
        label = f'({slope}, {y_intercept})'
        plt.plot(x_values, y_values, label=label)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Plot of lines")
    plt.legend()
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.savefig(figure_path)
    plt.close()

def contour_map(df, figure_path):
    contour = plt.tricontourf(df['Slope'], df['Y-intercept'], df['Cost'], cmap='viridis')
    plt.colorbar(contour, label='Cost')
    plt.xlabel('Slope')
    plt.ylabel('Y-intercept')
    plt.title('Cost Function Contour Plot')
    plt.savefig(figure_path)
    plt.close

def main():
    print("main()")

if __name__ == '__main__':
    main()