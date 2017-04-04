function data_type (input){
	if (typeof input === 'string'){
		output = input.length;
	}

	else if (typeof input === 'undefined'){
		output = "No Value";

	}
	
	else if (typeof input === 'boolean'){
		output = boolean(input);

	}

	else if (typeof input === 'number'){
		if (input < 100){
			output = "less than 100";
		}
		else{
			output = "more than 100";
		}
	}

	else if (value instanceof input){
		output = input[3];

	}

	else (input  === 'function'){
		output = input(true);

	}

	return output;

}