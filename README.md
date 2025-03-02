# goit-algo-hw-05
Home work in scope of Basic Algorithms and Data Structures module

# Порівняння алгоритмів пошуку підрядка

## Стаття 1: Пошук існуючого рядка
| Алгоритм              | Час виконання (сек) |
|------------------------|--------------------|
| **Boyer-Moore**       | 0.000705           |
| **Knuth-Morris-Pratt** | 0.003330           |
| **Rabin-Karp**        | 0.008053           |

## Стаття 2: Пошук існуючого рядка
| Алгоритм              | Час виконання (сек) |
|------------------------|--------------------|
| **Boyer-Moore**       | 0.004365           |
| **Knuth-Morris-Pratt** | 0.024469           |
| **Rabin-Karp**        | 0.049450           |

## Стаття 1: Пошук неіснуючого рядка
| Алгоритм              | Час виконання (сек) |
|------------------------|--------------------|
| **Boyer-Moore**       | 0.002812           |
| **Knuth-Morris-Pratt** | 0.021246           |
| **Rabin-Karp**        | 0.049413           |

## Стаття 2: Пошук неіснуючого рядка
| Алгоритм              | Час виконання (сек) |
|------------------------|--------------------|
| **Boyer-Moore**       | 0.004396           |
| **Knuth-Morris-Pratt** | 0.029602           |
| **Rabin-Karp**        | 0.072530           |


# Висновки щодо швидкості алгоритмів пошуку підрядка

## Стаття 1
- **Пошук існуючого рядка:**  
  Найшвидшим алгоритмом є **Boyer-Moore** (0.000705 с), що значно перевершує Knuth-Morris-Pratt (0.003330 с) і Rabin-Karp (0.008053 с).
- **Пошук неіснуючого рядка:**  
  Boyer-Moore знову лідирує (0.002812 с), демонструючи стабільну ефективність навіть у випадках невдалого пошуку.

## Стаття 2
- **Пошук існуючого рядка:**  
  **Boyer-Moore** (0.004365 с) залишається найшвидшим, хоча розрив між алгоритмами більший, ніж у першій статті.
- **Пошук неіснуючого рядка:**  
  Boyer-Moore знову перевершує інших (0.004396 с), що вказує на його ефективність для всіх випадків пошуку.

## Загальні висновки
- **Boyer-Moore** – найефективніший у всіх тестах, завдяки використанню евристик, які дозволяють пропускати частини тексту.
- **Knuth-Morris-Pratt** працює швидше, ніж Rabin-Karp, але поступається Boyer-Moore.
- **Rabin-Karp** – найповільніший через додаткові обчислення хеш-функцій.

### **Висновок:**  
**Алгоритм Boyer-Moore є найкращим вибором для швидкого пошуку підрядків у великих текстах.**
