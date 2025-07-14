    function runAll() {
      let num1 = 12;
      let num2 = 6;
      let text = "GOA";
      let isTrue = true;
      let fruits = ["Mango", "banana", "whatermelon"];
      let user = {name: "Tika", age: 25};

      let sum = num1 + num2;
      let diff = num1 - num2;
      let mult = num1 * num2;
      let div = num1 / num2;

      console.log("+", sum);
      console.log("-", diff);
      console.log("*", mult);
      console.log("/", div);

      console.log("== :", num1 == num2);
      console.log("=== :", num1 === num2);
      console.log("!= :", num1 != num2);
      console.log("!== :", num1 !== num2);
      console.log("< :", num1 < num2);
      console.log("<= :", num1 <= num2);
      console.log("> :", num1 > num2);
      console.log(">= :", num1 >= num2);

      const wantsToLeave = confirm("Do you want to leave the site?");
      if (wantsToLeave) {
        console.log("you will leave the site soon");
      } else {
        console.log("you are staying on the site");
      }
    }