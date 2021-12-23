# Khai báo các thư viện
import matplotlib.pyplot as plt

# Thiết lập chế độ vẽ
fig = plt.figure()
ax = plt.axes(projection = '3d')

# Tọa độ điểm nối chân thứ nhất với thân của robot
Px = 0
Py = 0
Pz = 0;
ax.plot3D(Px, Py, Pz, marker = ".", color = "red")
ax.text(Px, Py, Pz, 'P')

# Vẽ hệ tọa độ tại điểm nối chân thứ nhất với thân của robot
ax.plot3D([Px, Px + 2], [Py, Py], [Pz, Pz], linewidth = 0.5, color="red")
ax.plot3D([Px, Px], [Py, Py + 2], [Pz, Pz], linewidth = 0.5, color="green")
ax.plot3D([Px, Px], [Py, Py], [Pz, Pz + 2], linewidth = 0.5, color="blue")
Ax = Px
Ay = Py
Az = Pz + 1;
ax.plot3D(Ax, Ay, Az, marker = ".", color = "red")
ax.text(Ax, Ay, Az, 'A')
ax.text(2, 0, 0, 'x')
ax.text(0, 2, 0, 'y')
ax.text(0, 0, 2, 'z')

# Vẽ các điểm trên chân thứ nhất
Bx = Px
By = Py + 1
Bz = Pz
ax.plot3D(Bx, By, Bz, marker = ".", color = "red")
ax.text(Bx, By, Bz, 'B')
ax.plot3D([Px, Bx], [Py, By], [Pz, Bz], linewidth = 2, color="orange")
Cx = Bx
Cy = By
Cz = Bz - 0.5
ax.plot3D(Cx, Cy, Cz, marker = ".", color = "red")
ax.text(Cx, Cy, Cz, 'C')
ax.plot3D([Bx, Cx], [By, Cy], [Bz, Cz], linewidth = 2, color="orange")
Dx = Cx - 0.5
Dy = Cy
Dz = Cz - 0.8
ax.plot3D(Dx, Dy, Dz, marker = ".", color = "red")
ax.text(Dx, Dy, Dz, 'D')
ax.plot3D([Cx, Dx], [Cy, Dy], [Cz, Dz], linewidth = 2, color="orange")
Ex = Cx + 0.5
Ey = Cy
Ez = Cz - 1.5
ax.plot3D(Ex, Ey, Ez, marker = ".", color = "red")
ax.text(Ex, Ey, Ez, 'E')
ax.plot3D([Dx, Ex], [Dy, Ey], [Dz, Ez], linewidth = 2, color="orange")

# Vẽ các điểm và đường tham chiếu
Fx = Cx
Fy = Cy
Fz = Ez
ax.plot3D(Fx, Fy, Fz, marker = ".", color = "red")
ax.text(Fx, Fy, Fz, 'F')
ax.plot3D([Px, Ex], [Py, Ey], [Pz, Ez], linewidth = 0.5, color="green", linestyle='dashed')
ax.plot3D([Px, Fx], [Py, Fy], [Pz, Fz], linewidth = 0.5, color="green", linestyle='dashed')
ax.plot3D([Bx, Ex], [By, Ey], [Bz, Ez], linewidth = 0.5, color="green", linestyle='dashed')
ax.plot3D([Cx, Ex], [Cy, Ey], [Cz, Ez], linewidth = 0.5, color="green", linestyle='dashed')
ax.plot3D([Cx, Ex], [Cy, Ey], [Cz, Ez], linewidth = 0.5, color="green", linestyle='dashed')
ax.plot3D([Cx, Fx], [Cy, Fy], [Cz, Fz], linewidth = 0.5, color="green", linestyle='dashed')
ax.plot3D([Ex, Fx], [Ey, Fy], [Ez, Fz], linewidth = 0.5, color="green", linestyle='dashed')

# Hiển thị
ax.set_xlim(-1, 3.5); ax.set_ylim(-1, 3.5); ax.set_zlim(-2.5, 2)
plt.axis('off')
ax.grid(False)
plt.show()
