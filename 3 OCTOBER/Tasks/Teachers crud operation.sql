use University

switched to db University

db.Teachers.insertOne({
  teacher_id: 1,
  name: "Anamika",
  age: 21,
  city: "Mumbai",
  course: "AI",
  marks: 95
})

db.Teachers.insertMany([
  {student_id: 2,name: "Priya",age: 30,city: "Dehli",subject: "AI"},
  {student_id: 3,name: "Shashi",age: 32,city: "Bengaluru",subject: "ML"},
  {student_id: 4,name: "Sangeeta",age: 29,city: "Hyderabad",subject: "CA"},
  {student_id: 5,name: "Megha",age: 31,city: "Kolkata",subject: "Data Analysis"},
])

db.Teachers.find()

db.Teachers.findOne({name:"Shashi"})

db.Teachers.findOne({age: {$gt:32} })

db.Teachers.find({}, {name:1,course:1,_id:0})

db.Teachers.updateOne(
  {name: "Sangeeta"},
  {$set: { age: 19, subject: "Advanced Deep Learning"}}
)

db.Teachers.updateMany(
  {subject: "ML"},
  {$set: { grade: "A"}}
)

db.Teachers.deleteOne(
  {name: "Anamika"}
)

db.students.deleteMany(
  {marks: { $lt: 80}}
)