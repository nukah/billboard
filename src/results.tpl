<form action='/edit' method='POST' name='updatelist'>
<table>
%if r:
%   for index, entry in enumerate(r):
<tr id='{{ index }}'>
<td>Enabled: <input type='checkbox' name='status{{index}}' checked='yes'></td>
<td>Title: <input name='title{{index}}' type='text' value='{{ entry['title'] }}'></td>
<td>Date: <input name='date{{index}}' type='text' value='{{ entry['date']}}' size='12'></td>
<td>Time: <input name='time{{index}}' type='text' value='{{ entry['time']}}' size='5'></td>
<td>Link: <input name='link{{index}}' type='text' value='{{ entry['link'] }}'></td>
<td>Description: <textarea name='descr{{index}}' cols='40' rows='5'>{{ entry['description'] }}</textarea></td>
<td>Image: <input type='file' name='pic{{index}}' value = 'Image'></td> 
</tr>
%end
</table>
<input type='hidden' name='amount' value='{{ len(r) }}'>
<input type='submit' value='Write!'>
</form>
