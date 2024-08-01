# Bunker - reversing

plug Bunker.jar that into an online java deocmpiler <http://www.javadecompilers.com/> using fernflower

click on the .java file and find the following code

```java
if (!this.output.equals("72945810")) {
    JOptionPane.showMessageDialog((Component)null, "=== BUNKER CODE INVALID ===");
}
```

endter the code `72945810` into the java app and get the flag

`flag{bunker_11_says_await_further_instruction}`
