# This is a VERY broad yara file, and due to the immense amout of rules needed top cover all languages, this is just POC
# However, although this does not cover all languages, it can catch many languages in a more broader aspect (Will not know the language, but will know it is a script of some sort)

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
        $function_define = "function " nocase | "def " nocase | "sub " nocase | "fn " nocase
        
        // Detect class definitions across various languages
        $class_define = "class " nocase | "module " nocase
        
        // Detect import or include statements
        $import = "import " nocase | "require " nocase | "#include " nocase

        // Detect comments in various scripting languages
        $comment = "#" nocase | "//" nocase | "/*" nocase

        // Detect variable initialization across different languages
        $variable_initilization = "let " nocase | "var " nocase | "const " nocase

        // Detect variable types in languages that use typing
        $variable_type = "int " nocase | "float " nocase | "string " nocase | "bool " nocase | "char " nocase

        // Detect print statements across different languages
        $print_statement = "print(" nocase | "printf(" nocase | "echo " nocase

    condition:
        any of them
}