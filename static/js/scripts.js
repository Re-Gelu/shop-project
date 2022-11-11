/* var sum = 2 + 5;
var result = 100 < 1000 && 100 > 0;
console.log(result);

function print_hello() {
  console.log("Hello world");
} */

class User {
	#name
	#age

	constructor(name, age) {
		this.#name = name
		this.#age = age
	}

	get name() {return this.#name}
	get age() {return this.#age}
	set age(value) {
		if (0 <= value <=100){
			this.#age = value
		}
	}

	get_main_info() {return `Name: ${this.name}, Age: ${this.age}`}
}

class Employee extends User {
	#company

	constructor(name, age, company) {
		super(name, age)
		this.#company = company
	}

	get_main_info() {return `${super.get_main_info()}, Company: ${this.#company}`}
}


var TestUser = new User("One", 18)
TestUser.age = 20
console.log(TestUser.get_main_info())

var TestEmployee = new Employee("Second", 21, "yandex")
console.log(TestEmployee.get_main_info());

const person = "tom";

function check (parts, name) {
	console.log(parts);
	return parts[0] + name + parts[1];
}

let checkedTemplate = check`Person: ${person}`;
console.log(checkedTemplate);
document.body.innerHTML = checkedTemplate;