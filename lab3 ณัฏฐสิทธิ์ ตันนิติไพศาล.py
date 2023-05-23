import random
import tkinter as tk
from tkinter import messagebox


class Food:
    def __init__(self, name, calories, protein, sodium):
        self.name = name
        self.calories = calories # kilocalories
        self.protein = protein # gram
        self.sodium = sodium # gram

class Dessert:
    def __init__(self, name, calories, sugar):
        self.name = name
        self.calories = calories # kilocalories
        self.sugar = sugar # gram

class Drink:
    def __init__(self, name, calories, sugar):
        self.name = name
        self.calories = calories # kilocalories
        self.sugar = sugar # gram

class Fruit:
    def __init__(self, name, calories, protein):
        self.name = name
        self.calories = calories # kilocalories
        self.protein = protein

def random_food(list_food):
    selected_food = random.sample(list_food, 3)
    result_food_cal = selected_food[0].calories + selected_food[1].calories + selected_food[2].calories
    return selected_food, result_food_cal


def random_muscle_food(muscle_list_food):
    selected_muscle_food = random.sample(muscle_list_food, 3)
    result_food_cal = selected_muscle_food[0].calories + selected_muscle_food[1].calories + selected_muscle_food[2].calories
    return selected_muscle_food, result_food_cal

def random_diet_food(diet_list_food):
    selected_diet_food = random.sample(diet_list_food, 3)
    result_food_cal = selected_diet_food[0].calories + selected_diet_food[1].calories + selected_diet_food[2].calories
    return selected_diet_food, result_food_cal

def random_dessert(list_dessert):
    selected_dessert = random.sample(list_dessert, 2)
    result_dessert_cal = selected_dessert[0].calories + selected_dessert[1].calories
    return selected_dessert, result_dessert_cal

def random_drink(list_drink):
    selected_drink = random.choice(list_drink)
    result_drink_cal = selected_drink.calories
    return selected_drink, result_drink_cal

def random_fruit(list_fruit):
    selected_fruit = random.sample(list_fruit, 2)
    return selected_fruit

def random_workout_activity():
    activities = [
        { "name": "วิ่งเล่นรอบสวน", "calories": 300 },
        { "name": "กระโดดเชือก", "calories": 400 },
        { "name": "ยกแขนด้วยน้ำหนัก","calories": 500 },
        { "name": "เล่นแบดมินตัน",  "calories": 350 },
        { "name": "จักรยานเสือภูเขา",  "calories": 450 },
        { "name": "ยิมนาสติก", "calories": 550 },
        { "name": "ว่ายน้ำ", "calories": 700 },
        { "name": "เล่นบาสเกตบอล", "calories": 600 },
        { "name": "เตะฟุตบอล", "calories": 650 },
        { "name": "เต้นลีลาศ", "calories": 400 },
    ]

    random_activity = random.choice(activities)
    return random_activity

def random_suggest():
    suggest_list = [
        { "name": "ทิป : คุณควรบริโภคอาหารที่มีสารอาหารสูงแต่ให้พลังงานจำกัด", "type": "yes" },
        { "name": "ทิป : คุณควรรักษาน้ำหนักตัวให้อยู่ในระดับที่เหมาะสม", "type": "yes" },
        { "name": "ทิป : คุณควรออกกำลังกายเป็นประจำ", "type": "yes" },
        { "name": "ทิป : คุณควรกินผักผลไม้และนมไขมันเป็นประจำ", "type": "yes" },
        { "name": "ทิป : คุณควรบริโภคไขมันในปริมาณน้อย", "type": "yes" },
        { "name": "ทิป : คุณควรกินอาหารที่มีกากใยสูง", "type": "yes" },
        { "name": "ทิป : คุณควรลดการบริโภคอาหารที่มีเกลือและกินอาหารที่มีโปแตสเชี่ยมสูง", "type": "yes" },
        { "name": "ทิป : คุณควรหลีกเลี่ยงเครื่องดื่มที่มีแอลกอฮอล์", "type": "yes" },
        { "name": "ทิป : คุณควรเก็บรักษาและเตรียมอาหารโดยคำนึงถึงความปลอดภัยเป็นหลัก", "type": "yes" },
        { "name": "ทิป : คุณควรหลีกเลี่ยงการกินอาหารรสหวานจัดและเค็มจัด", "type": "yes" },
        ]

    random_suggest = random.choice(suggest_list)
    return random_suggest

def create_gui():
    # Define the lists of food, dessert, drink, and fruit
    list_food = [Food("ข้าวผัดกะเพรา", 450, 20, 1.1),
                 Food("ข้าวไข่เจียว", 300, 12.5, 0.4),
                 Food("ผัดไทยกุ้งสด", 400, 30, 1.1),
                 Food("ไก่ย่างผักโขมอบชีส", 375, 32.5, 0.6),
                 Food("สลัดผัก", 125, 6, 0.3),
                 Food("ปลานึ่งมะนาว", 175, 22.5, 0.3),
                 Food("ข้าวต้มกุ้ง", 200, 15, 1),
                 Food("ผัดผักบุ้ง", 250, 9, 0.1),
                 Food("ปลาแซลมอน", 175, 19, 0.06),
                 Food("อกไก่", 160, 27.5, 0.05),
                 Food("ข้าวผัดหมู", 400, 12.5, 0.75),
                 Food("ควินัว", 500, 40, 0.7),
                 Food("สปาเกตตี้", 300, 22.5, 0.4),
                 Food("แกงส้มชะอมทอด", 375, 17.5, 0.9),
                 Food("แซนวิชทูน่า", 260, 25, 0.5)]
    diet_list_food = [food for food in list_food if food.calories < 300]
    muscle_list_food = [food for food in list_food if food.protein > 15]
    list_dessert = [Dessert("บัวลอย", 100, 10),
                    Dessert("ทับทิมกรอบ", 120, 15),
                    Dessert("ขนมชั้น", 150, 20),
                    Dessert("ไอศกรีมวนิลลา", 137, 14.5),
                    Dessert("พุดดิ้ง", 64, 12),
                    Dessert("เค้ก", 235, 22),
                    Dessert("พาย", 160, 16),
                    Dessert("โดนัท", 76, 19),
                    Dessert("บราวนี่", 150, 17),
                    Dessert("ข้าวเหนียวมะม่วงว", 330, 31)]
    list_drink = [Drink("น้ำเปล่า", 0, 0),
                  Drink("โค้ก", 150, 30),
                  Drink("น้ำส้มคั้น", 100, 25),
                  Drink("ชาเขียวเย็น", 109.5, 11.3),
                  Drink("กาแฟเย็น", 108.5, 9.8),
                  Drink("เป๊ปซี่", 200, 19),
                  Drink("ชานมไข่มุก", 190, 17),
                  Drink("โกโก้", 150, 13)]
    list_fruit = [Fruit("ส้ม", 50, 0.9),
                  Fruit("แอปเปิ้ล", 60, 0.3),
                  Fruit("กล้วย", 80, 1.1),
                  Fruit("สตรอเบอร์รี่", 49, 0.7),
                  Fruit("องุ่น", 104, 0.6),
                  Fruit("มะม่วง ", 98, 0.8),
                  Fruit("ทุเรียน ", 163, 1.47),
                  Fruit("แก้วมังกร ", 85, 1.4)]
    GENDER_OPTIONS = ["Male", "Female"]
    FOOD_OPTIONS = ["General", "Muscle", "Diet"]


        # Create a GUI window
    window = tk.Tk()
    window.title("Random Food and Workout Generator")

    # Create a label for the selected food
    welcome_label = tk.Label(window, text="ยินดีต้อนรับเข้าสู่แอพกินอะไรดี:", font=("Arial", 18, "bold"), fg="blue")
    welcome_label.pack()

    blank_label = tk.Label(window, text="")
    blank_label.pack()

    selected_gender = tk.StringVar()
    selected_gender.set(GENDER_OPTIONS[0])

    gender_label = tk.Label(window, text="Selected Gender:", font=("Arial", 10, "bold"))
    gender_label.pack()

    gender_option_menu = tk.OptionMenu(window, selected_gender, *GENDER_OPTIONS)
    gender_option_menu.pack()

    selected_cat = tk.StringVar()
    selected_cat.set(FOOD_OPTIONS[0])

    cat_label = tk.Label(window, text="Selected food category:", font=("Arial", 10, "bold"))
    cat_label.pack()

    cat_option_menu = tk.OptionMenu(window, selected_cat, *FOOD_OPTIONS)
    cat_option_menu.pack()

    food_label = tk.Label(window, text="Randomed Food:", font=("Arial", 10, "bold"))
    food_label.pack()

    food_name = tk.Label(window, text="", font=("Arial", 10))
    food_name.pack()

    blank_label = tk.Label(window, text="")
    blank_label.pack()

    # Create a label for the selected dessert
    dessert_label = tk.Label(window, text="Randomed Dessert:", font=("Arial", 10, "bold"))
    dessert_label.pack()
    dessert_name = tk.Label(window, text="", font=("Arial", 10))
    dessert_name.pack()

    blank_label = tk.Label(window, text="")
    blank_label.pack()

    # Create a label for the selected drink
    drink_label = tk.Label(window, text="Randomed Drink:", font=("Arial", 10, "bold"))
    drink_label.pack()
    drink_name = tk.Label(window, text="", font=("Arial", 10))
    drink_name.pack()

    blank_label = tk.Label(window, text="")
    blank_label.pack()

    # Create a label for the selected fruits
    fruit_label = tk.Label(window, text="Randomed Fruits:", font=("Arial", 10, "bold"))
    fruit_label.pack()
    fruit_names = tk.Label(window, text="", font=("Arial", 10))
    fruit_names.pack()

    blank_label = tk.Label(window, text="")
    blank_label.pack()

    # Create a label for the total calories
    total_calorie_label = tk.Label(window, text="Total Calories:", font=("Arial", 10, "bold"))
    total_calorie_label.pack()
    total_calorie_value = tk.Label(window, text="", font=("Arial", 10))
    total_calorie_value.pack()

    blank_label = tk.Label(window, text="")
    blank_label.pack()

    calorie_notification = tk.Label(window, text="", font=("Arial", 10, "bold"), fg="red")
    calorie_notification.pack()
    protein_notification = tk.Label(window, text="", font=("Arial", 10))
    protein_notification.pack()

    blank_label = tk.Label(window, text="")
    blank_label.pack()

    warn_label = tk.Label(window, text="คุณสามารถทำตามกิจกรรมต่อไปนี้เพื่อลดปริมาณแคลอรี่สะสม", font=("Arial", 10, "bold"))
    warn_label.pack()

    workout_label = tk.Label(window, text="Randomed Workout Activity:", font=("Arial", 10, "bold"))
    workout_label.pack()
    workout_name = tk.Label(window, text="", font=("Arial", 10))
    workout_name.pack()
    calories_label = tk.Label(window, text="Calories Burned (cal/hour):", font=("Arial", 10, "bold"))
    calories_label.pack()
    calories_value = tk.Label(window, text="", font=("Arial", 10))
    calories_value.pack()

    suggest_name = tk.Label(window, text="", font=("Arial", 10, "bold"))
    suggest_name.pack()


    # Create a button to generate random items

    generate_button = tk.Button(window, text="Generate", command=lambda: generate_items(), font=("Arial", 12, "bold"), fg="blue")
    generate_button.pack()

    # Generate random items and update the GUI labels
    def generate_items():
        selected_food, food_cal = random_food(list_food)
        selected_muscle = random_muscle_food(muscle_list_food)
        selected_dessert, dessert_cal = random_dessert(list_dessert)
        selected_drink, drink_cal = random_drink(list_drink)
        selected_fruit = random_fruit(list_fruit)

        if selected_cat.get() == "General" :
                food_name.config(text=f"มื้อเช้า: {selected_food[0].name} ({selected_food[0].calories} kcal)\n"
                                      f"มื้อกลางวัน: {selected_food[1].name} ({selected_food[1].calories} kcal)\n"
                                      f"มื้อเย็น: {selected_food[2].name} ({selected_food[2].calories} kcal)\n"
                                      f"รวม ({food_cal} kcal)")
        elif selected_cat.get() == "Muscle":
                food_name.config(text=f"มื้อเช้า: {selected_food[0].name} ({selected_food[0].calories} kcal)\n"
                                      f"มื้อกลางวัน: {selected_food[1].name} ({selected_food[1].calories} kcal)\n"
                                      f"มื้อเย็น: {selected_food[2].name} ({selected_food[2].calories} kcal)\n"
                                      f"รวม ({food_cal} kcal)")
        elif selected_cat.get() == "Diet":
                food_name.config(text=f"มื้อเช้า: {selected_food[0].name} ({selected_food[0].calories} kcal)\n"
                                      f"มื้อกลางวัน: {selected_food[1].name} ({selected_food[1].calories} kcal)\n"
                                      f"มื้อเย็น: {selected_food[2].name} ({selected_food[2].calories} kcal)\n"
                                      f"รวม ({food_cal} kcal)")


        selected_dessert, dessert_cal = random_dessert(list_dessert)
        dessert_name.config(text=f"ระหว่างมื้อแรก: {selected_dessert[0].name} ({selected_dessert[0].calories} kcal)\n"
                                 f"ระหว่างมื้อสอง: {selected_dessert[1].name} ({selected_dessert[1].calories} kcal)\n"
                                 f"รวม ({dessert_cal} kcal)")

        selected_drink, drink_cal = random_drink(list_drink)
        drink_name.config(text=f"{selected_drink.name} ({drink_cal} kcal)")

        selected_fruit = random_fruit(list_fruit)
        fruit_names.config(text=f"ระหว่างมื้อสาม: {selected_fruit[0].name} ({selected_fruit[0].calories} kcal)\n "
                                f"ก่อนนอน: {selected_fruit[1].name} ({selected_fruit[1].calories} kcal)")

        total_calories = food_cal + dessert_cal + drink_cal + selected_fruit[0].calories + selected_fruit[1].calories
        total_calorie_value.config(text=f"{total_calories} kcal")
        total_sugar = selected_dessert[0].sugar + selected_dessert[1].sugar + selected_drink.sugar
        total_sodium = selected_food[0].sodium + selected_food[1].sodium + selected_food[2].sodium
        total_protein = selected_food[0].protein + selected_food[1].protein + selected_food[2].protein + selected_fruit[0].protein + selected_fruit[1].protein


        if selected_gender.get() == "Male" and total_calories > 1600:
            excess_calories = total_calories - 1600
            notification = f"คำเตือน!!!\nคุณได้รับแคลอรี่เกินไป {excess_calories} kcal จากที่กำหนด (1600 kcal)"
            if total_sugar > 25:
                excess_sugar = total_sugar - 25
                notification += f"\nคุณได้รับน้ำตาลเกินไป {excess_sugar} กรัม"
            if total_sodium > 1.5:
                excess_sodium = total_sodium - 1.5
                notification += f"\nคุณได้รับโซเดียมเกินไป {excess_sodium} กรัม"
            messagebox.showinfo("คำเตือน", notification)
            calorie_notification.config(text=notification)
        elif selected_gender.get() == "Female" and total_calories > 1300:
            excess_calories = total_calories - 1300
            notification = f"คำเตือน!!!\nคุณได้รับแคลอรี่เกินไป {excess_calories} kcal จากที่กำหนด (1300 kcal)"
            if total_sugar > 25:
                excess_sugar = total_sugar - 25
                notification += f"\nคุณได้รับน้ำตาลเกินไป {excess_sugar} กรัม"
            if total_sodium > 1.5:
                excess_sodium = total_sodium - 1.5
                notification += f"\nคุณได้รับโซเดียมเกินไป {excess_sodium} กรัม"
            messagebox.showinfo("คำเตือน", notification)
            calorie_notification.config(text=notification)

        activity = random_workout_activity()
        workout_name.config(text=activity["name"])
        calories_value.config(text=str(activity["calories"]))

        suggestion = random_suggest()
        suggest_name.config(text=suggestion["name"])

        if selected_cat.get() == "Muscle" and total_protein < 100:
            sever_protein = 100 - total_protein
            notifications = f"คุณได้รับโปรตีนน้อยไป {sever_protein} กรัม สำหรับการสร้างกล้ามเนื้อ\nพวกเราแนะนำให้คุณกิน {selected_food[0].name} เพิ่มนะ"
            protein_notification.config(text=notifications)

    # Run the GUI event loop
    window.mainloop()

# Create the GUI
create_gui()

