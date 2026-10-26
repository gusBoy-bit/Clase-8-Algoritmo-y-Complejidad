**Priority Queues y Hash Tables**



Actividad:

Resolución de dos desafíos de LeetCode utilizando estructuras de datos en Python.



Ejercicio 1: Kth Largest Element in an Array



\- Estructura: Priority Queue

\- Dificultad: Media

\- Enlace: https://leetcode.com/problems/kth-largest-element-in-an-array/

\- Archivo: "kth\_largest.py"



Descripción: Se debe encontrar el k-ésimo elemento más grande dentro de una lista de números enteros.



Solución: Se empleó una cola de prioridad mediante "heapq", manteniendo los k elementos mayores y eliminando los menores cuando se supera el tamaño establecido.



Complejidad temporal: O(n log k).



Complejidad espacial: O(k).



Ejercicio 2: Contains Duplicate



\- Estructura: Hash Table

\- Dificultad: Fácil

\- Enlace: https://leetcode.com/problems/contains-duplicate/

\- Archivo: "contains\_duplicate.py"



Descripción: Se debe verificar si una lista contiene algún número repetido.



Solución: Se utilizó un conjunto (set) para registrar los números encontrados. Si un elemento ya pertenece al conjunto, se devuelve True; de lo contrario, se continúa hasta terminar el recorrido.



Complejidad temporal: O(n) en promedio.



Complejidad espacial: O(n).



Conclusión:

Los ejercicios permitieron comprender la aplicación de las colas de prioridad y las tablas hash. La primera estructura permite mantener elementos organizados por prioridad, mientras que la segunda facilita la identificación rápida de valores previamente almacenados.

