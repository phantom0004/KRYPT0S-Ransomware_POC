// This is a VERY broad Yara file, and due to the immense amount of rules needed to cover all languages, this is just a POC.
// Although this does not cover all languages, it can detect scripts in a broader sense (It may not identify the language but will detect that it is a script).

rule scripting_languages_detection
{
    meta:
        author = "Daryl Gatt"
        description = "Detects common scripting languages, focuses on common scripting languages."
        date = "2024-09-13"

    strings:
        // Common Shebangs
        $python_bin_shebang = "#!/usr/bin/python" nocase 
        $python_env_shebang = "#!/usr/bin/env python"
        $bash_shebang = "#!/bin/bash" nocase
        $perl_shebang = "#!/usr/bin/perl" nocase
        $lua_shebang = "#!/usr/bin/lua" nocase

        // Common file properties - Python
        $python_import = "import " 
        $python_exception = "except"
        $python_main = "def main():"
        $python_lambda = "lambda "  // Python lambda expressions
        $python_self = "self"  // Used in class methods

        // Common file properties - C & C++
        $c_include = "#include " 
        $c_cpp_main = "int main("
        $cpp_namespace = "namespace " 
        $c_import = "#include <stdio.h>"
        $cpp_import = "#include <iostream>" 
        $cpp_string = "std::cout <<"
        $c_string = "printf("
        $c_return = "return 0;"  // Common in C/C++ to indicate successful completion

        // Common file properties - Ruby
        $ruby_require = "require "
        $ruby_module = "module "
        $ruby_puts = "puts "
        $ruby_end = "end"  // Marks the end of a block or method
        $ruby_yield = "yield"  // Ruby keyword for passing control

        // Common file properties - Perl
        $perl_use = "use "  // For module imports in Perl
        $perl_sub = "sub "  // For defining subroutines in Perl
        $perl_strict = "use strict;"  // Perl strict mode

        // Common file properties - Haskell
        $haskell_main = "main = "  // Main function in Haskell

        // Common file properties - Go (Golang)
        $go_package = "package "  // Package declaration in Go
        $go_import = "import ("  // Import multiple packages in Go
        $go_main = "func main()"  // Main function in Go

        // Common Characteristics
        $python_and_ruby_function = "def "  // Shared function definition keyword

    condition:
        any of them
}

rule identify_script_file
{
    meta:
        author = "Daryl Gatt"
        description = "If the 'scripting_languages_detection' rule fails, will resort to this to see if file is a script."
        date = "2024-09-13"

    strings:
        // Detect function definitions across various languages
        $function_define_1 = "function " nocase
        $function_define_2 = "def " nocase
        $function_define_3 = "sub " nocase
        $function_define_4 = "fn " nocase

        // Detect class definitions across various languages
        $class_define_1 = "class " nocase
        $class_define_2 = "module " nocase

        // Detect import or include statements
        $import_1 = "import " nocase
        $import_2 = "require " nocase
        $import_3 = "#include " nocase

        // Detect comments in various scripting languages
        $comment_1 = "#" nocase
        $comment_2 = "//" nocase
        $comment_3 = "/*" nocase

        // Detect variable initialization across different languages
        $variable_init_1 = "let " nocase
        $variable_init_2 = "var " nocase
        $variable_init_3 = "const " nocase

        // Detect variable types in languages that use typing
        $variable_type_1 = "int " nocase
        $variable_type_2 = "float " nocase
        $variable_type_3 = "string " nocase
        $variable_type_4 = "bool " nocase
        $variable_type_5 = "char " nocase

        // Detect print statements across different languages
        $print_statement_1 = "print(" nocase
        $print_statement_2 = "printf(" nocase
        $print_statement_3 = "echo " nocase

    condition:
        any of them
}
