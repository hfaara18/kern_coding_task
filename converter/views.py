# import from django
from django.shortcuts import render, redirect
from django.views.generic import View

# importing custom forms
from .forms import StringForm, DNATemplateForm

# import from codec
from .codec.encoding.encode import encode
from .codec.encoding.decode import decode

# other imports
import json

# empty forms to be shown
DEFAULT_CONTEXT = {
    'string_form': StringForm(),
    'dna_template_form': DNATemplateForm(),
}

# Conversions - a class that handles what the user sees on the page.
#               The class sends objects to be displayed on the page
#               based on whether the user submits a query.
class Conversions(View):
    def get(self, request):
        return render(request, 'converter/index.html', context=DEFAULT_CONTEXT)

    def post(self, request):
        context = DEFAULT_CONTEXT
        # getting data from the submitted forms
        string_form = StringForm(request.POST)
        dna_template_form = DNATemplateForm(request.POST)
        # initializing the nucleotide counts dict
        nucleotide_counts = {}
        # an objects to be sent to the page
        nucleotide_counts_json = json.dumps(nucleotide_counts)

        # processing a StringForm submissions
        if string_form.is_valid():
            # parsing input from StringForm query
            input_string = string_form.cleaned_data['input_string']

            try:
                processed_input_string = encode(input_string)
                nucleotide_counts = get_nucleotide_counts("".join(processed_input_string))
                nucleotide_counts_json = json.dumps(nucleotide_counts)
            except:
                processed_input_string = 'The input string was invalid'
            context.update({'processed_input_string': processed_input_string,
                            'nucleotide_counts_json': nucleotide_counts_json})
        else:
            context.update({'processed_input_string': '',
                            'nucleotide_counts_json': nucleotide_counts_json})

        # processing a DNATemplateForm submissions
        if dna_template_form.is_valid():
            # parsing input from DNATemplateForm query
            input_dna_templates = dna_template_form.cleaned_data['input_dna_templates'].split(',')
            input_dna_templates = [i.strip(" ") for i in input_dna_templates]

            try:
                processed_input_dna_templates = decode(input_dna_templates)
            except:
                processed_input_dna_templates = 'The input DNA template was invalid'
            context.update({'processed_input_dna_templates': processed_input_dna_templates})
        else:
            context.update({'processed_input_dna_templates': ''})

        # passing objects to be displayed on cenversion page
        return render(request, 'converter/index.html', context=context)

# input: string - a string of nucleotides
# output: dictionary - a dictionary with nucleotides as keys and the counts as values
def get_nucleotide_counts(joined_templates):
    nucleotide_counts = {"A":0, "C":0, "G":0, "T":0}
    for nucleotide in joined_templates:
        nucleotide_counts[nucleotide] = nucleotide_counts.get(nucleotide, 0) + 1

    nucleotide_counts = {i[0]:i[1] for i in sorted(nucleotide_counts.items(), key = lambda x:x[0])}
    return nucleotide_counts
