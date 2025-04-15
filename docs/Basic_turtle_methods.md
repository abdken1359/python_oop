Welcome to Python Turtle! It's a fun way to learn programming while creating cool drawings. Here are some common methods you can use with the `turtle` module:

### Basic Setup

1. **`turtle.Turtle()`**  
   Creates a new turtle object.
   
   ```python
   t1 = turtle.Turtle()
   ```

2. **`turtle.Screen()`**  
   Creates a screen object (for background color, etc.).
   
   ```python
   screen = turtle.Screen()
   ```

### Common Methods for the Turtle Object

1. **`t1.color("color_name")`**  
   Sets the turtle’s color. You can use color names (like `"red"`, `"blue"`) or RGB values.
   
   ```python
   t1.color("blue")
   ```

2. **`t1.forward(distance)`**  
   Moves the turtle forward by a specified distance.
   
   ```python
   t1.forward(100)
   ```

3. **`t1.backward(distance)`**  
   Moves the turtle backward by a specified distance.
   
   ```python
   t1.backward(50)
   ```

4. **`t1.left(angle)`**  
   Turns the turtle left by a certain angle (in degrees).
   
   ```python
   t1.left(90)
   ```

5. **`t1.right(angle)`**  
   Turns the turtle right by a certain angle.
   
   ```python
   t1.right(90)
   ```

6. **`t1.penup()`**  
   Lifts the pen, so the turtle moves without drawing.
   
   ```python
   t1.penup()
   ```

7. **`t1.pendown()`**  
   Lowers the pen, so the turtle starts drawing again.
   
   ```python
   t1.pendown()
   ```

8. **`t1.setposition(x, y)`**  
   Moves the turtle to an absolute position `(x, y)` on the screen.
   
   ```python
   t1.setposition(100, 100)
   ```

9. **`t1.goto(x, y)`**  
   Moves the turtle to the given (x, y) coordinates.
   
   ```python
   t1.goto(-50, 50)
   ```

10. **`t1.speed(speed)`**  
    Sets the turtle’s drawing speed (from 1 to 10 or `fastest`, `normal`, `slowest`).
    
    ```python
    t1.speed(3)
    ```

11. **`t1.circle(radius)`**  
    Makes the turtle draw a circle with a specified radius.
    
    ```python
    t1.circle(50)
    ```

12. **`t1.begin_fill()`**  
    Starts filling the shape drawn with the current color.
    
    ```python
    t1.begin_fill()
    ```

13. **`t1.end_fill()`**  
    Ends the fill operation (completes the shape).
    
    ```python
    t1.end_fill()
    ```

14. **`t1.shape("shape_name")`**  
    Changes the turtle’s shape. Options include `"turtle"`, `"triangle"`, `"classic"`, `"square"`, and `"arrow"`.
    
    ```python
    t1.shape("turtle")
    ```

15. **`t1.stamp()`**  
    Stamps the turtle’s shape at the current position on the screen.
    
    ```python
    t1.stamp()
    ```

16. **`t1.write(text)`**  
    Writes text at the turtle’s current position.
    
    ```python
    t1.write("Hello, Turtle!")
    ```

17. **`t1.hideturtle()`**  
    Hides the turtle (the drawing pen is still visible).
    
    ```python
    t1.hideturtle()
    ```

18. **`t1.showturtle()`**  
    Makes the turtle visible again.
    
    ```python
    t1.showturtle()
    ```

These methods will allow you to draw, move, and customize your turtle's behavior. Feel free to experiment with them and combine them to create fun shapes and designs! Let me know if you'd like examples of specific things you want to do.
