+++
title = "Resource Acquisition is Initialization"
lastmod = 2021-06-16T12:17:52-07:00
draft = false
+++

RAII is a [Programming]({{<relref "programming.md" >}}) paradigm which states that resources (e.g. memory) should be accessed via classes. This means that the class's constructor allocates the resources, and its destructor deallocates it.

Here is an example of not using RAII:

```c++
RawResourceHandle* handle=createNewResource();
handle->performInvalidOperation();  // Oops, throws exception
...
deleteResource(handle); // oh dear, never gets called so the resource leaks
```

Notice that you get a memory leak.

Here is an example using RAII:

```c++
class ManagedResourceHandle {
public:
   ManagedResourceHandle(RawResourceHandle* rawHandle_) : rawHandle(rawHandle_) {};
   ~ManagedResourceHandle() {delete rawHandle; }
   ... // omitted operator*, etc
private:
   RawResourceHandle* rawHandle;
};

ManagedResourceHandle handle(createNewResource());
handle->performInvalidOperation();
```

Notice that if an exception is thrown, the resource is still deallocated. This makes it memory safe.

What's more, when the object leaves scope, the resource is automatically deallocated.