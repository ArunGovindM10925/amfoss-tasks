var message = "Hi"; //spam message 
var interval = Math.random(); //sets the interval to a random number less than 1
var count = Math.floor(Math.random() * 100) + 1; //returns a random integer from 1 to 100, is the number of times to send
var notify = count ; //notify 
var i = 0 ;
var timer = setInterval(function(){
	document.getElementsByClassName('composer_rich_textarea')[0].innerHTML = message;
	$('.im_submit').trigger('mousedown');	
	i++;
	if( i  == count )
	clearInterval(timer);
	if( i % notify == 0)
	console.log(i + ' MESSAGES SENT');
} , interval * 1000 ) ;