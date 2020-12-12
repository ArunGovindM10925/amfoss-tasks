//Instructions
//Go to https://web.telegram.org/. Go to your friend's chat, press F12, paste the code into the console. Press enter.
//Program
var message = "Hi"; //spam message 
var interval = Math.random(); //sets the interval to a random number less than 1
var count = Math.floor(Math.random() * 100) + 1; //returns a random integer from 1 to 100, is the number of times to send
var notify = count ; //notify 
var i = 0 ;
var timer = setInterval(function(){
	document.getElementsByClassName('composer_rich_textarea')[0].innerHTML = message;	//copies the message into the text box
	$('.im_submit').trigger('mousedown');	//triggers a mousedown event in the submit button
	i++;	//keeps the count of messages
	if( i  == count )	//if i reaches the desired number of times, it stops the iteration
	clearInterval(timer);
	if( i % notify == 0)	//after the iteration stops, the line displays the number of messages sent in the console
	console.log(i + ' MESSAGES SENT');
} , interval * 1000 ) ;	//keeps on iterating after interval*1000 milliseconds
