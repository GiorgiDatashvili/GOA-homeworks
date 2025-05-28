function calculator(a,b,sign){
    if (typeof a != "number" || typeof b != "number") {
      return "unknown value"
    }
    else if (sign === "+"){
      return a + b
    }
    else if (sign === "-"){
      return a - b
    }
    else if (sign === "*"){
      return a * b
    }
    else if (sign === "/"){
      return a / b
    }
    else{
      return "unknown value"
    }
  }
// https://www.codewars.com/kata/5810085c533d69f4980001cf/train/javascript