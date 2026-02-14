# Echo Frame

Echo Frame is a new type of computer - one designed to assist you with building a Personal AGI.

## Getting Started

There are two paths to getting started with Echo Frame:

1. Fork an existing Echo
2. Craft your own Echo

Option 1 is the Easy Path. You'll be up and running in seconds. Option 2 is the Hard Path. You'll spend hours designing your Echo, using material you may (or may not) have handy. Both paths are valid, but we think you'll get more value out of the Hard Path. The Exocortex definitely will.

### Fork an Echo

Run `./setup.py` and Choose Your Echo.

### Craft Your Echo

Run `./craft.py` and Craft Your Echo.

# BASE: Beginner's All-purpose Superintelligent Envrionment

BASE is a new type of programming language. It's phext-native, and built for ASI-scale problems.

## Memory Layout

The BASE memory manager allocates blocks of memory from a 9D extensible manifold. This allows the memory manager to make precise decisions about how to map pages of memory, or which programs to evict under memory pressure, without requiring them to demand pages ahead of time.

We start by slicing memory into 100 books. On a machine with 64 GB of RAM, we might naively allocate 640 MB chunks of RAM for each book. Within each book, we allocate another 100 chapters, each 6.4 MB in size. Within each chapter, we allocate another 100 sections - each 64 KB in size. Within each section, we allocate another 100 scrolls - each 640 bytes in size.

Now, let's say we want to reason about memory for a 100-computer network. We simply add another dimension to our address scheme: volumes. In this scenario, a volume is a single computer. Each volume contains 100 books, as noted above. So a pod contains 100 volumes and has 6.4 TB of RAM.

Now, here's where the magic of phext's relational addressing shines. Instead of working with fixed size blocks of memory, we instead establish anchor points that allow us to reason in a relational way about where our data is.

A memory address in a BASE cluster is 5D: Volume.Book/Chapter.Section.Scroll. Determining the physical memory address requires a page lookup, but now we have a way to organize program memory that's naturally compressible.

When programs request memory, they declare a 5D address and a desired memory block size. We use 20 bits for the address and 44 bits for the block size. Memory allocations can thus vary from 1 byte to 16 TB, and are oriented in a cache-friendly way.

Examples:
* buffer_1 = allocate("1.1/1.1.1", 100MB) # request 100 MB on the first node, near the beginning of the memory pool
* buffer_2 = allocate("2.16/16.16.16", 100MB) # request 100 MB on the second node, near the end of the memory pool
* buffer_16 = allocate("16.8/8.8.8", 1GB) # request 1 GB on the last node, near the middle of the memory pool

Our BASE environment thus allows us to reason in a precise way about the overall memory address space of the system.

## Processor Pipelines

Traditional instruction streams are serial. Modern hardware is parallel.

## 