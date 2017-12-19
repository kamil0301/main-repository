import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import patches as mpaths
import json

# program obrazujący w postaci animacji tor ruchu auta w kolejnych sekundach ruchu na podstawie położenia pocz
# położenia końcowego i prędkości
#
#ZAD_DOM:
#  - dodaj ściany
#  - dodaj opóźnienia (PRE_EVACUATION)


class Pedestrian:
    def __init__(self, goals, velo):
        self.traj = []
        #self.start = (0, 0)
        self.speed = velo
        #self.traj.append(self.start)
        self.goals = goals

    def create_vel_vector(self, actual, goal):
        vec_real = np.array(goal) - np.array(actual)  # wspolrzedne wektorow rzeczywistych aby z warunku brało goals_no
        len_vec_real = np.linalg.norm(vec_real)
        vec_u = vec_real / len_vec_real
        vec_vel = vec_u * self.speed
        return vec_vel

    def create_trajectory(self, actual, goal):
        vec_vel = self.create_vel_vector(actual, goal)

        x = actual[0] + vec_vel[0]
        y = actual[1] + vec_vel[1]
        position = (x, y)
        self.traj.append(position)
        return position, vec_vel

    def do_it(self):
        goal_no = 0
        position, vec_vel = self.create_trajectory(self.goals[goal_no], self.goals[goal_no +1])

        while True:             #pętla tworząca trajektorię
            try:
                if np.linalg.norm(self.goals[goal_no] - np.array(position)) <= self.speed:
                    goal_no += 1
                position, vec_vel = self.create_trajectory(position, self.goals[goal_no])
            except:
                break

        return self.traj

    def chart(self):
        self.do_it()
        x, y = zip(*self.traj)
        plt.plot(x, y, "-o")
        plt.show()


class Pedestrians:
    def __init__(self):
        self.peds = []

    def add_pedestrians(self, ped):
        self.peds.append(ped)
        print(self.peds)

    def get_trajectories(self):
        trajectories = []
        for i in self.peds:
            trajectories.append(i.do_it())
        return trajectories

    def get_chart(self):
        trajs = self.get_trajectories()
        temp_traj = []
        lens = []

        for i in trajs:
            lens.append(len(i))
        length = max(lens)
        for i in range(length):          # dla iluśtam kroków
            step = []
            for j in range(len(trajs)):  # tworzy gdzie są w danym kroku
                try:
                    step.append(trajs[j][i])
                except:
                    step.append(trajs[j][-1])
            temp_traj.append(step)          #do tego momentu tworzy odpowiednią trajektorię
        print(temp_traj)

        foo = zip(*temp_traj)               #rysuje trajektorie
        for i in foo:
            x, y = zip(*i)
            plt.plot(x, y, "-")

        return temp_traj


class Animation:
    def __init__(self, pedest):
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(0, 60), ylim=(0, 20))
        self.n_frames = 0
        self.trial = []
        self.ang = 0

        self.trajectory = pedest.get_chart()
        self.n_frames = len(self.trajectory)

        elipses = [mpaths.Ellipse(i, width=1, height=1, angle=self.ang) for i in
                   self.trajectory[0]]      # stworzenie kształtu i przypisanie mu cech (wymiary, współ początkowych)
        [self.trial.append(self.ax.add_patch(elipses[i])) for i in range(len(elipses))]

    def init_animation(self):
        [self.trial[i].set_visible(True) for i in range(len(self.trial))]

        return self.trial

    def animate(self, i):
        for j in range(len(self.trajectory[0])):
            self.trial[j].center = self.trajectory[i][j]
        return self.trial

    def do_animation(self, n_interval):
        animate = anim.FuncAnimation(self.fig, self.animate, frames=self.n_frames, init_func=self.init_animation,
                                     interval=n_interval, blit=True)
        plt.show()


def change_data(eggman_ped):
    vel = eggman_ped["H_SPEED"]
    goals = []
    goals.append(eggman_ped['ORIGIN'])
    goals.extend(eggman_ped['ROADMAP'])

    return goals, vel


file1 = open("//home/wojtas/PythonFiles/main-repository/Python - zadania/ewakuacja2/eggman.json", 'r')
first_floor = json.load(file1)["1"]["EVACUEES"]
#file2 = open("C:\pliki_py\geom.json", "r")
#obst = json.load(file2)["obstacles"]["1"]


a = Pedestrians()
for i in first_floor:
    print(change_data(first_floor[i]))
    temp_ped = Pedestrian(*change_data(first_floor[i]))
    a.add_pedestrians(temp_ped)

x = Animation(a)
x.do_animation(100)
