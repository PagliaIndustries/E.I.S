# E.I.S
<h1>Electronic Inventory System</h1>

<p>
This is the Electronic Inventory System.
It can be used to keep track of all your items and works with a USB (plug/play) barcode scanner.
</p>

<h2>Install/Setup</h2>
<p>
To install this program you can either:
  <ul>
    <li>Download the exe app and run it (Easiest) (The App Can Be Found Under Releases)</li>
    <li>Download all the files and make an exe app yourself (With pyinstaller (Use the LoginScreen.py as the file to make exe))</li>
    <li>Download all the files and run the program from the terminal</li>
    </ul>
</p>

<p><b>
The program's default Login is: <br>
Admin<br>
1234<br>
(This can be changed in the Settings Menu)
</b></p>

<h3>Features</h3>
<ul>
<li>You can set low quanity reminders for each item's subcategory, that way you can be notified on the program's startup on what needs to be ordered</li>
<li>The program also calculates the total prices of your total inventory (with/without markup).</li>
<li>You can Add/Remove items</li>
<li>You can Checkout/Return items</li>
</ul>

<ul>
Markup Values are Hardcoded
  <li>#Markup Values:</li>
  <li>#0-$49.99         50%</li>
  <li>#$50-149.99       45%</li>
  <li>#$150-999.99      35%</li>
  <li>#$1,000-1,999.99  30%</li>
  <li>#$2,000-2,999.99  20%</li>
  <li>#$3,000-3,999.99  15%</li>
  <li>#$4,000 or Higher 10%</li>
  #Located in calculate_sellprice() in AdminMenu.py 
</ul>

<h4>Program Snapshots</h4>

![EIS Demo Pic](https://user-images.githubusercontent.com/115889137/234100559-42fb64b0-8bc8-431f-851f-07fcaaa85983.png)

![Screenshot (25)](https://user-images.githubusercontent.com/115889137/207741161-2d7f9947-78e7-4cbc-810e-84b8ea751485.png)

![Screenshot (29)](https://user-images.githubusercontent.com/115889137/207741690-25335dfe-0e39-4ec9-b9da-063f3cf181cb.png)
![Screenshot (26)](https://user-images.githubusercontent.com/115889137/207741692-7a73f963-5ea9-4638-aeae-5c2a9baadfea.png)
![Screenshot (28)](https://user-images.githubusercontent.com/115889137/207741693-a14a4048-3887-49d8-b60d-58ef8aebd627.png)

