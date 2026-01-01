Don't edit these files since they may be overwritten by an upstream pull. Copy them to your own assignment folder.

Pro tip; writing lots of data to the console can be really hard to process. For task 1/3 you can use
ASCII codes to control the terminal a little better. These are commands to your terminal emulator.
Understanding these is beyond this course (and, really, quite archaic these days), but they work

// Clear the screen and move the cursor to the top left / origin. The flush makes sure its not buffered, thats all
// use this before your loop of motor states
System.out.print("\033[H\033[2J"); System.out.flush();

// Move to the origin. Use this before you print your motor states so they just update in place on screen
System.out.print("\033[H");  // move to origin

