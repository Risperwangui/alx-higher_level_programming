#include <Python.h>

/**
 * print_python_list_info -prints info about python lists
 * @p: a python list
 */
void print_python_list_info(PyObject *p)
{
	int size, list, a;
	PyObject *obj;

	size = Py_SIZE(p);
	list = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", list);

	for (a = 0; a < size; a++)
	{
		printf("Element %d; ", a);

		obj = PyList_GetItem(p, a);
		printf("%s\n", Py_TYPE(obj->tp_name);
	}
}
