# Databricks notebook source
class lib:
    def __init__(self):
        pass

    @staticmethod
    def some_lib_function(*args):
        print(*args)

    @staticmethod
    class some_namespace_class:
        def __init__(self):
            self.name = "some nested class"
            print(self.name)
