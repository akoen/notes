+++
title = "Test-Driven Development"
lastmod = 2021-06-16T12:20:17-07:00
draft = false
+++

-   Why don't more languages implement tests directly in the functions themselves? For example, in Eiffel:

    ```prog
    put (x: ELEMENT; key: STRING) is
    		-- Insert x so that it will be retrievable through key.
    	require
    		count <= capacity
    		not key.empty
    	do
    		... Some insertion algorithm ...
    	ensure
    		has (x)
    		item (key) = x
    		count = old count + 1
    	end
    ```

    -   This is somewhat implemented in languages like Java with assert() statements