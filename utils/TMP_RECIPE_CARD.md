<!-- How to use comments in these files -->
<!-- ---------------------------------- -->
<!--Comments have been put in this file so that they can be customised for a range of workshops and uses.

[How to customise the Markdown documents](CustomMarkdown.md)-->

<!---#include "RECIPE_CARD.txt"--->


<!---#define RC_RECIPE_COLOUR GREEN--->
<!---#define RC_GITHUB_URL https://raw.githubusercontent.com/PiHw/Pi-Kitchen/master/sdcard--->


<img src="img/pihwlogotm.png" width=180 />
<hr>

<img style="float:left" src="img/PiKitchenRecipe.png" width=180 />
#Recipe Card#

<!---#ifdef RC_NUMBER--->
<!---#ifdef RC_NAME--->
<font color = RC_RECIPE_COLOUR>
<h1>RC_NUMBER : RC_NAME</h1>
</font>
<!---#endif--->
<!---#endif--->

<table style="width:35%" align="right" >
  <tr>
    <th bgcolor=black><font color=white>Recipe Files</th>		
    <th bgcolor=black><font color=white>Ingredients</th>
  </tr>
  <tr>
    <td>
    <!---#ifdef RC_BOOT--->
      <i><b><a href="RC_GITHUB_URL/RC_SOURCE_LOCATION/RECIPE_FILE_boot.txt">(flavour)_boot.txt</a></i></b><p>
    <!---#endif--->
    <!---#ifdef RC_ROOT--->
      <i><b><a href="RC_GITHUB_URL/RC_SOURCE_LOCATION/RECIPE_FILE_root.txt">(flavour)_root.txt</a></i></b><p>
    <!---#endif--->
    <!---#ifdef RC_DATA--->
      <i><b><a href="RC_GITHUB_URL/RC_SOURCE_LOCATION/RECIPE_FILE_data.txt">(flavour)_data.txt</a></i></b><p>
    <!---#endif--->
    </td>		
    <td><i><b><a href="RC_GITHUB_URL/recipes/RC_ZIP">RC_ZIP</a></i></b></td>
  </tr>
</table>

<br>
<!---#ifdef RC_DESC--->
##Description##
<font color = RC_RECIPE_COLOUR>
<!--RC_DESC<p> Moved description from RECIPE_CARD.txt to README.md file-->
<!---#include "README.md"--->
</font>
<!---#endif--->

<!---#ifdef RC_HOWTOUSE--->
##How to use##
<font color = RC_RECIPE_COLOUR>
RC_HOWTOUSE<p>
</font>
<!---#endif--->

##Ingredients##
Unless otherwise stated files should be placed in the following location on the NOOBS RECOVERY partition:<p>

<font color = RC_RECIPE_COLOUR>
RC_SOURCE_LOCATION<p>
</font>

This recipe uses the following files:<p>
<font color = RC_RECIPE_COLOUR>
RC_INGREDIENTS<p>
</font>

<!---#ifdef RC_INGREDIENTS_SETTING--->
<b>Plus the following files in the _SETTINGS folder:</b><p>

It is assumed that the following file(s) are placed in the following location on the NOOBS RECOVERY partition:<p>
<font color = RC_RECIPE_COLOUR>
<code>RC_SOURCE_LOCATION_SETTING</code><p>
</font>

You will need the following _SETTINGS file(s):<p>

<font color = RC_RECIPE_COLOUR>
RC_INGREDIENTS_SETTING<p>
</font>

<img style="float:left" src="img/note.png" height=40/>
<b>NOTE:</b> Files which are configured manually or may contain sensitive information are placed in the _SETTTINGS directory on the SD-Card.  This is so that it is easier to support different configurations and remove sensitive information from the setup if needed.<p>

<!---#ifdef RC_SETTING_DESC--->
Perform the following actions:<p>
<font color = RC_RECIPE_COLOUR>
RC_SETTING_DESC<p>
</font>
<!---#endif--->
<!---#endif--->

You can download all the <a href="RC_GITHUB_URL/recipes/RC_ZIP">ingredient files</a>, and extract directly to the NOOBS SD-Card (ensuring you remove the ZIP file's name from the directory - the files should be extracted to <code>/Pi-Kitchen</code>).<p>

##The Recipe Files##
Each recipe will use one file for each of the partitions it installs to - boot, root and data).<p>

<!---#ifdef RC_DATA--->
<img style="float:left" src="img/note.png" height=40/>
<b>NOTE:</b> The data partition does not normally exist for most installations unless manually selected.  However you can also include this partition automatically if desired (see the <a href="http://pihw.wordpress.com/guides/pi-kitchen/automaticinstallations">Pi-Kitchen: Automatic Installations</a> guide for more details).<p>
<!---#endif--->

You will need to suitably rename or copy the content of each of the following files into your recipe files (i.e. <code>RaspbianPiKitchen_root.txt</code>) and place them in your os folder in the NOOBS partition (i.e. <code>os/Raspbian</code>).<p>

For more information see the <a href="http://pihw.wordpress.com/guides/pi-kitchen/creatingflavours">Pi-Kitchen: Creating Flavours</a> guide.<p>

<!---#ifdef RC_BOOT--->
<i><b><a href="RC_GITHUB_URL/RC_SOURCE_LOCATION/RECIPE_FILE_boot.txt">(flavour)_boot.txt</a></i></b>
<pre>
<!---#include RECIPE_FILE_boot.txt--->
</pre>
<!---#endif--->

<!---#ifdef RC_ROOT--->
<i><b><a href="RC_GITHUB_URL/RC_SOURCE_LOCATION/RECIPE_FILE_root.txt">(flavour)_root.txt</a></i></b>
<pre>
<!---#include RECIPE_FILE_root.txt--->
</pre>
<!---#endif--->

<!---#ifdef RC_DATA--->
<i><b><a href="RC_GITHUB_URL/RC_SOURCE_LOCATION/RECIPE_FILE_data.txt">(flavour)_data.txt</a></i></b>
<pre>
<!---#include RECIPE_FILE_data.txt--->
</pre>
<!---#endif--->


<hr>

Enjoy baking your Raspberry Pi SD-Card fresh from the Pi-Kitchen.<p>

<!--========================END FILE================-->