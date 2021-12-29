import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#

##############GLOBAL API#################
# # A SIMPLE EXAMPLE OF GLOBAL API (INVOKING FUNCTIONS AT MODULE LEVEL(PLT))
# # print(x)
#
# plt.figure(figsize=(6, 6))
# plt.title("Sample Plot 1")
#
# plt.plot(x, x ** 2, "g")
# plt.plot(x, -1 * (x ** 2), "r")
#
# # A BIT COMPLEX EXAMPLE OF GLOBAL API
# plt.figure(figsize=(12, 6))
# plt.title("Sample plot 2")
#
# plt.subplot(1, 2, 1) # rows, columns and panel selected
# plt.plot(x, x ** 2, "g")
# plt.plot([0, 0, 0], [-10, 10, 100], "r")
# plt.legend(["X^2", "Vertical Line"])
# plt.xlabel("X")
# plt.ylabel("X Squared")
#
# plt.subplot(1, 2, 2)
# plt.plot(x, -1 * (x ** 2), "g")
# plt.plot([-10, 0, 10], [-50, -50, -50], "r")
# plt.legend(["-X^2", "Horizontal line "])
# plt.xlabel("X")
# plt.ylabel("X Squared")
##############GLOBAL API#################

################OOP INTERFACE##################
# # SINGLE AXIS SAMPLE PLOT
# fig, axis = plt.subplots(figsize=(12, 6))
# axis.plot(x, (x ** 2), color="red", linewidth=3, marker="o", markersize=8, label="X^2")
# axis.plot(x, -1 * (x ** 2), "b--", label="-X^2")
# axis.set_xlabel("X")
# axis.set_ylabel("X Squared")
# axis.set_title("Sample Plot 3")
# axis.legend()
# print(fig)

# # MULTIPLE AXIS SAMPLE PLOT
# fig_1, axis_1 = plt.subplots(figsize=(12, 6))
# axis_1.plot(x, x + 0, linestyle="solid")
# axis_1.plot(x, x + 1, linestyle="dashed")
# axis_1.plot(x, x + 2, linestyle="dashdot")
# axis_1.plot(x, x + 3, linestyle="dotted")
# axis_1.set_title("Sample Plot 4")
# print(fig_1)

# # ANOTHER MULTIPLE AXIS SAMPLE PLOT
# fig, axis_2 = plt.subplots(figsize=(12, 6))
# axis_2.plot(x, x + 0, "-og", label="solid green")
# axis_2.plot(x, x + 1, "--c", label="dashed cyan")
# axis_2.plot(x, x + 2, "-.b", label="dashdot blue")
# axis_2.plot(x, x + 3, ":r", label="dotted red")
# axis_2.set_title("Sample Plot 5")
# axis_2.legend()

# Different types of lines and markers
# print("Markers: {}".format([m for m in plt.Line2D.markers]))
# linestyles = ["_", "-", "--", ":"]
# print("Line styles: {}".format(linestyles))
#
# # When we call subplots() we get a tuple containing a Figure and a axis element
# plot_objects = plt.subplots()
# fig, ax = plot_objects
# ax.plot([1, 2, 3], [1, 2, 3])
# print(plot_objects)
#
# # Plotting multiple graphs on the same figure (in this case its 4)
# plt_objects = plt.subplots(nrows=2, ncols=2, figsize=(14, 6))
# fig, ((ax1, ax2), (ax3, ax4)) = plt_objects
# ax1.plot(np.random.randn(50), c="red", linestyle="--")
# ax2.plot(np.random.randn(50), c="green", linestyle=":")
# ax3.plot(np.random.randn(50), c="blue", marker="o", linewidth=3.0)
# ax4.plot(np.random.randn(50), c="yellow")
# print(fig)

# # You can make a grid of your choice to display the graphs
# plt.figure(figsize=(14, 6))
# ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
# ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
# ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
# ax4 = plt.subplot2grid((3, 3), (2, 0))
# ax5 = plt.subplot2grid((3, 3), (2, 1))
################OOP INTERFACE##################

# Scatter Plot
# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
# area = np.pi * (20 * np.random.rand(N)) ** 2  # 0 to 15 point radii
# plt.figure(figsize=(14, 6))
# plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap="Spectral")
# plt.colorbar()
##############

# # Histogram
# values = np.random.rand(1000)
# plt.subplots(figsize=(12, 6))
# plt.hist(values, bins=100, alpha=0.8, histtype="bar",
#          color="blue", edgecolor="green")
# plt.xlim(xmin=-5, xmax=5)
###########

# # KDE
# values = np.random.rand(1000)
# density = stats.kde.gaussian_kde(values)
# plt.subplots(figsize=(12, 6))
# values2 = np.linspace(min(values)-10, max(values)+10, 100)
# plt.plot(values2, density(values2), color="#FF7F00")
# plt.fill_between(values2, 0, density(values2), alpha=0.5, color="#FF7F00")
# plt.xlim(xmin=-5, xmax=5)
###############

# # Bar Plot
# Y = np.random.rand(1, 5)[0]
# Y2 = np.random.rand(1, 5)[0]
# plt.figure(figsize=(12, 4))
# barWidth=0.5
# plt.bar(np.arange(len(Y)), Y, width=barWidth, color="#00b894", label="Label Y")
# # Stacking 2 Bar Plots
# plt.bar(np.arange(len(Y2)), Y2, width=barWidth, color="#e17055", bottom=Y, label="Label Y2")
# plt.legend()
################

# # Outlier detection using Box Plot
# values = np.concatenate([np.random.rand(10), np.array([10, 15, -10, -15])])
# plt.figure(figsize=(12, 4))
# plt.boxplot(values)
###################

plt.show()
