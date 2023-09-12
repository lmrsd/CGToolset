import ix

def get_all_context(ignoreDisabled=False):

    prj = ix.get_item('project:/')

    # get all contexts
    all_contexts = ix.api.OfContextSet()
    ignore_disabled_ctx = ignoreDisabled

    if ignore_disabled_ctx:
        mask = ix.api.CoreBitFieldHelper(ix.api.OfIten.FLAG_NONE, ix.api.OfIten.FLAG_NONE, ix.api.CoreBitFieldHelper.MODE_DISABLE, ix.api.CoreBitFieldHelper.MODE_DISABLE)
        prj.resolve_all_contexts(all_contexts, mask)
    else:
        prj.resolve_all_contexts(all_contexts)

    return all_contexts

def get_refences_context(context_list):

    ref_ctx = [context_list[i] for i in range(context_list.get_count()) if context_list[i].is_reference()]

    
    return ref_ctx

