const age = document.querySelector('.age-form.box-shape');
const form = document.querySelector('.form');


// form.addEventLister('submit', () => validator(e))

// function validator(e){
// 	if (value && Number(age.value) < 30){
// 		e.preventDefault()
// 		alert("Age must be more than 30 years")
// 	}
// }

form.addEventListener('submit', (e) => {
	e.preventDefault();
	
	if ( age && Number(age.value) < 30) {		
		alert('Age must be 30 and above')
	} else {
		return true
	}
})