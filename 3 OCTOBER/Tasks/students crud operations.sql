db
test
use University
switched to db University
db.Student.insertOne({})
{
  acknowledged: true,
  insertedId: ObjectId('68dfa4079e4e4cf0648b2d62')
}
db.Student.insertOne({
  student_id: 1,
  name: "Rahul",
  age: 21,
  city: "Mumbai",
  course: "AI",
  marks: 95
})
{
  acknowledged: true,
  insertedId: ObjectId('68dfa4949e4e4cf0648b2d63')
}
db.students.insertMany(
  {student_id: 1,name: "Rahul",age: 21,city: "Mumbai",course: "AI",marks: 95},
)
db.students.insertMany(
  {student_id: 1,name: "Rahul",age: 21,city: "Mumbai",course: "AI",marks: 95},
)
MongoInvalidArgumentError: Argument "docs" must be an array of documents
db.students.insertMany([
  {student_id: 2,name: "Priya",age: 21,city: "Dehli",course: "AI",marks: 95},
  {student_id: 3,name: "Ranvijay",age: 22,city: "Bengaluru",course: "ML",marks: 85},
  {student_id: 4,name: "Abhyraj",age: 20,city: "Hyderabad",course: "CA",marks: 78},
  {student_id: 4,name: "Gaurav",age: 23,city: "Kolkata",course: "Data Analysis",marks: 67},
])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68dfa6c29e4e4cf0648b2d64'),
    '1': ObjectId('68dfa6c29e4e4cf0648b2d65'),
    '2': ObjectId('68dfa6c29e4e4cf0648b2d66'),
    '3': ObjectId('68dfa6c29e4e4cf0648b2d67')
  }
}
d.students.find()
ReferenceError: d is not defined
db.students.find()
{
  _id: ObjectId('68dfa6c29e4e4cf0648b2d64'),
  student_id: 2,
  name: 'Priya',
  age: 21,
  city: 'Dehli',
  course: 'AI',
  marks: 95
}
{
  _id: ObjectId('68dfa6c29e4e4cf0648b2d65'),
  student_id: 3,
  name: 'Ranvijay',
  age: 22,
  city: 'Bengaluru',
  course: 'ML',
  marks: 85
}
{
  _id: ObjectId('68dfa6c29e4e4cf0648b2d66'),
  student_id: 4,
  name: 'Abhyraj',
  age: 20,
  city: 'Hyderabad',
  course: 'CA',
  marks: 78
}
{
  _id: ObjectId('68dfa6c29e4e4cf0648b2d67'),
  student_id: 4,
  name: 'Gaurav',
  age: 23,
  city: 'Kolkata',
  course: 'Data Analysis',
  marks: 67
}
db.students.findOne({name:"Ranvijay"})
{
  _id: ObjectId('68dfa6c29e4e4cf0648b2d65'),
  student_id: 3,
  name: 'Ranvijay',
  age: 22,
  city: 'Bengaluru',
  course: 'ML',
  marks: 85
}
db.students.findOne({marks: {$gt:85} })
{
  _id: ObjectId('68dfa6c29e4e4cf0648b2d64'),
  student_id: 2,
  name: 'Priya',
  age: 21,
  city: 'Dehli',
  course: 'AI',
  marks: 95
}
db.students.find({}, {name:1,course:1,_id:0})
{
  name: 'Priya',
  course: 'AI'
}
{
  name: 'Ranvijay',
  course: 'ML'
}
{
  name: 'Abhyraj',
  course: 'CA'
}
{
  name: 'Gaurav',
  course: 'Data Analysis'
}
db.students.updateOne(
  {name: "Abhyraj"},
  {$set: { marks: 99, course: "Advanced Deep Learning"}}
)
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
db.students.updateMany(
  {course: "ML"},
  {$set: { grade: "A"}}
)
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
db.students.deleteOne(
  {name: "Abhyraj"}
)
{
  acknowledged: true,
  deletedCount: 1
}
db.students.deleteMany(
  {marks: { $lt: 80}}
)
