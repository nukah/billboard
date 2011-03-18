<form action='/choose' method='POST'>
Add Event <input type='radio' name='event'>
Add Feed <input type='radio' name='feed'>
<input type='submit' value='Choose!'>
</form>

%for element in result:
{{ element }}
%end
