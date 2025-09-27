// #1
let number = 67
number = 41
console.log(number)
// #2
let num1 = 10
let num2 = 5
    if (num1>num2){
        console.log(`${num1} is higher than ${num2}`)
    }
    else{
        console.log(`${num2} is higher than ${num1}`)
    }
// 3
console.log(num1 + num2)
console.log(num1 - num2)
console.log(num1 * num2)
console.log(num1 / num2)
console.log(num1 % num2)
// 4
function logOp(nmb1,nmb2){
    if (nmb1 > nmb2 && nmb1 / nmb2 == 0){
        return "True"
    }
    else{
        return "False"
    }
}
console.log(logOp(67,41))

// 5
function bigNumbers(number){
    if (number > 10000000000000){
        return "Thats a big number"
    }
    else if (number < 10000000000000){
        return "Thats not a big number :(("
    }
    else{
        return "Thats the exact number !!!"
    }

}
console.log(bigNumbers(10000000000001))

// 6
function randomColor() {
    const colors = ["green","yellow","red"]
    const randomIndex = Math.floor(Math.random() * colors.length)
    return colors[randomIndex]
}
switch(randomColor()) {
    case "green":
        console.log("Go!");
        break;
    case "yellow":
        console.log("Wait...");
        break;   
    case "red":
        console.log("Stop!!!");
        break;
}
// 7
for (let i = 0;i < 11;i++){
    console.log(i)
}
let whileNum = 0
while (whileNum < 6){
    console.log(whileNum)
    whileNum++;
}
// 8
function addNums(numbr1,numbr2){
    return numbr1 + numbr2
}
console.log(addNums(535345435363,857284138138))

function greet(name){
    return `Hello, ${name}`
}
console.log(greet("Dexter Morgan"))
// 9
function ageChecker(age){
    if (age >= 18 && age < 60){
        return  `You are an adult 🧑 age - ${age}`
    }
    else if (age >= 60){
        return `You are a senior 👴 age - ${age}`
    }
    else{
        return `You are a teenager 👦 age - ${age}`
    }
}
const personAge = Math.floor(Math.random() * 101)
console.log(ageChecker(personAge))