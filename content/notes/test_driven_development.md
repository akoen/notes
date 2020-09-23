+++
title = "Test-Driven Development"
author = ["Alex Koen"]
lastmod = 2020-09-22T12:25:57-07:00
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
