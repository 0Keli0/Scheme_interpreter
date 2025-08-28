#Variables
ANTLR_JAR = ./interpreter_utils/antlr-4.13.2-complete.jar
GRAMMAR = scheme.g4
GEN_DIR = ./interpreter_utils
PYTHON = python3
SCHEME_INTERPRETER = scheme.py
SCHEME_PROGRAM_DIR = ./scheme_programs
SCHEME_PROGRAM_ALL = all
PROGRAM_INPUTS  = ./inout/input_files
PROGRAM_OUTPUTS = ./inout/output_files
PROGRAM_DIFF_OUTPUTS = ./inout/diff_output_files

#make all
all: setup options

options:
	@echo "clean: clean cache, antlr files generated and output files generated from tests"
	@echo "generate_tests: generate all tests with all the programs provided"
	@echo "antlr: generate parser and lexer with antlr4 command"
	@echo "run: run scheme_programs/all.scm program, that has all the test files in one"

setup:
	@echo "Setting up miniScheme Interpreter from grammar ${GRAMMAR} ... "
	java -jar ./interpreter_utils/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener  ${GEN_DIR}/${GRAMMAR}
	mkdir -p ${PROGRAM_OUTPUTS}     #Create directory in case it does not exist
antlr:
	@echo "Generate Parser and Lexer from grammar ${GRAMMAR} ..."
	antlr4 -Dlanguage=Python3 -no-listener -visitor  ${GEN_DIR}/${GRAMMAR}
run:
	${PYTHON} ${SCHEME_INTERPRETER} ${SCHEME_PROGRAM_DIR}/${SCHEME_PROGRAM_ALL}.scm < "${PROGRAM_INPUTS}/${SCHEME_PROGRAM_ALL}"_input.txt > "${PROGRAM_OUTPUTS}/${SCHEME_PROGRAM_ALL}"_output.txt
	diff "${PROGRAM_OUTPUTS}/${SCHEME_PROGRAM_ALL}"_output.txt "${PROGRAM_DIFF_OUTPUTS}/${SCHEME_PROGRAM_ALL}"_output.txt;


generate_tests:
		@echo "Running tests ..."
		@for test in $(wildcard ${SCHEME_PROGRAM_DIR}/*.scm); do \
                base=$$(basename $$test .scm); \
                echo "Running test $$base"; \
                echo ""${PROGRAM_INPUTS}/$$base"_input.txt"; \
                python3 ${SCHEME_INTERPRETER} $$test < "${PROGRAM_INPUTS}/$$base"_input.txt > "${PROGRAM_OUTPUTS}/$$base"_output.txt; \
        diff "${PROGRAM_OUTPUTS}/$$base"_output.txt "${PROGRAM_DIFF_OUTPUTS}/$$base"_output.txt; \
    done

clean:
	@echo "Cleaning generated files ..."
	rm -rf ${GEN_DIR}/*.interp ${GEN_DIR}/*.tokens
	find . -name "__pycache__" -exec rm -rf {} +
	rm -rf ${PROGRAM_OUTPUTS}
	rm ${GEN_DIR}/schemeVisitor.py ${GEN_DIR}/schemeLexer.py ${GEN_DIR}/schemeParser.py

.PHONY: all setup options antlr run generate_tests clean  #To specify they are not associated with files