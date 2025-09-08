
# 📚✨ Auto Class Planner ✨📅  

**Auto Class Planner** is a Python program that automatically generates a weekly class timetable 🏫.  
It balances subjects ⚖️, avoids duplicates ❌, adds a lunch break 🍲, and makes scheduling super easy 🔥.  

---

## 🌟 Features  

- 🎲 **Randomized Scheduling** – fresh timetable every run!  
- 📖 **Balanced Subjects** – each subject appears 3–4 times per week.  
- 🚫 **No Duplicates in a Day** – unique subjects daily.  
- 🍲 **Lunch Break Included** – automatically set after 3rd period.  
- ➕ **Add New Subjects Easily** – use `add_subject()` to customize.  

---

## 🖥️ Example Output  

```

Monday:
9am-9:45am: Maths
10am-10:45am: Physics
11am-11:45am: English
12pm-12:45pm: Lunch 🍲
1pm-1:45pm: Biology
2pm-2:45pm: History
3pm-3:45pm: Chemistry

````

---

## ⚙️ How It Works  

1. 📌 Define subjects, days, and time slots.  
2. 📊 Use a counter to track how many times each subject appears weekly.  
3. 🎲 Randomly assign subjects while following rules:  
   - ✅ No duplicate subjects per day.  
   - ✅ Subject limit (max 4 per week).  
4. 🍲 Insert **Lunch** automatically after the 3rd period.  
5. 🖨️ Print out the complete timetable for all weekdays.  

---

## 🚀 Future Improvements  

- 💾 Export timetable to CSV/Excel.  
- 🖼️ Add GUI/web interface for teachers & students.  
- ⭐ Subject priority (e.g., more Maths, less History).  
- 📅 Flexible max_classes rules per subject.  

---

## 🎯 Learning Purpose  

This project is perfect for:  
- 🐍 Practicing Python basics (lists, dicts, loops, functions).  
- 🎲 Using the `random` module for automation.  
- 🧩 Understanding scheduling logic & constraints.  

---

## ▶️ Run Instructions  

Clone the repo and run with:  

```bash
python auto_class_planner.py
````

---


