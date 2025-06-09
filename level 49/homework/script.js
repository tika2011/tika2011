        let name = "თემური";
        let age = 25;
        let isStudent = true;
        let hasJob = false;
        console.log("name:", name);
        console.log("age:", age);
        console.log("student:", isStudent);
        console.log("has job:", hasJob);

        let combined = name + "is" + age + " age. student" + isStudent + ", სამსახური აქვს? " + hasJob;
        console.log("test:", combined);

        function greet() {
            alert("hallo, " + name + "!");
        }