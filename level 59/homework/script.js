function check() {
      const cb1 = document.getElementById("cb1");
      const cb2 = document.getElementById("cb2");

      if (cb1.checked && cb2.checked) {
        let result = (cb1.value === cb2.value);
        document.getElementById("result").innerText = "Result of the operation is " + result;
        console.log("Result of the operation is " + result);
      } else {
        document.getElementById("result").innerText = "Please check both options.";
        console.log("Please check both options..");
      }}