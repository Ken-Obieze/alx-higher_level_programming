#include <Python.h>

/**
 * print_python_list_info - Prints information about python objects
 * @p: PyObject pointer to print info about
*/

void print_python_list_info(PyObject *p)
{
	int allocated, i, pl_size;
	PyObject *item;
	const char *i_type;
	PyListObject *list_object_cast;

	allocated  =  ((PyListObject *)p)->allocated;
	pl_size = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", pl_size);
	printf("[*] Allocated = %d\n", allocated);
	for (i = 0; i < pl_size; i++)
	{
		item = PyList_GetItem(p, i);
		i_type = Py_TYPE(item)->tp_name;
		printf("Element %d: %s\n", (int) i, i_type);
	}
}
