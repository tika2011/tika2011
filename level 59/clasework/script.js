 document.write1("true && false = " + (true && false) + "<br>");
 document.write2("true || false = " + (true || false) + "<br>");
 function convert() {
      let val = valInput.value;
      result.innerHTML =
        "ტექსტი: " + String(val) + "<br>" +
        "რიცხვი: " + Number(val) + "<br>" +
        "ლოგიკური: " + Boolean(val);
    }