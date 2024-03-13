import matplotlib.pyplot as plt

def statistika_tahlili(data):
    # Statistik ma'lumotlar tahlili va grafik yaratish
    plt.figure(figsize=(8, 5))

    # Grafikni yaratish
    plt.bar(data.keys(), data.values(), color='blue')

    # Diagramma sarlavhasi va x, y o'q nomlari
    plt.title("Statistik Ma'lumotlar Tahlili")
    plt.xlabel("X o'qi nomi")
    plt.ylabel("Y o'qi nomi")

    # Grafikni ko'rsatish
    plt.show()

if __name__ == "__main__":
    # Ma'lumotlar o'zgartirilganidan ma'lumotlarni o'zgartiring
    data = {"Guruh 1": 25, "Guruh 2": 30, "Guruh 3": 22, "Guruh 4": 18, "Guruh 5": 15}

    # Statistik ma'lumotlar tahlili va grafik yaratish
    print(statistika_tahlili(data))
