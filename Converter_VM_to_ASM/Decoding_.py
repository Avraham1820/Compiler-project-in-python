import os
import Comp_
import Flow_


def order(word0, word1, word2,labelCounter,currentClass,currentFunction):
    AsmStrOfFile = ''
    if word0 == 'push':
        if word1 == 'local':
            AsmStrOfFile += Comp_.push_seg_('LCL', word2)
        elif word1 == 'argument':
            AsmStrOfFile += Comp_.push_seg_('ARG', word2)
        elif word1 == 'this':
            AsmStrOfFile += Comp_.push_seg_('THIS', word2)
        elif word1 == 'that':
            AsmStrOfFile += Comp_.push_seg_('THAT', word2)

        elif word1 == 'pointer':
            AsmStrOfFile += Comp_.push_ptr_( word2)
        elif word1 == 'temp':
            AsmStrOfFile += Comp_.push_tmp_( word2)

        elif word1 == 'static':
            AsmStrOfFile += Comp_.push_static_(currentClass, word2)

        elif word1 == 'constant':
            AsmStrOfFile += Comp_.push_const_(word2)

    elif word0 == 'pop':
        if word1 == 'local':
            AsmStrOfFile += Comp_.pop_seg_('LCL', word2)
        elif word1 == 'argument':
            AsmStrOfFile += Comp_.pop_seg_('ARG', word2)
        elif word1 == 'this':
            AsmStrOfFile += Comp_.pop_seg_('THIS', word2)
        elif word1 == 'that':
            AsmStrOfFile += Comp_.pop_seg_('THAT', word2)

        elif word1 == 'pointer':
            AsmStrOfFile += Comp_.pop_ptr_(word2)
        elif word1 == 'temp':
            AsmStrOfFile += Comp_.pop_temp_(word2)

        elif word1 == 'static':
            AsmStrOfFile += Comp_.pop_static_(currentClass, word2)

        elif word1 == 'constant':
            AsmStrOfFile += Comp_.pop_const_(word2)

    elif word0 == 'add':
        AsmStrOfFile += Comp_.add_sub_('add')
    elif word0 == 'sub':
        AsmStrOfFile += Comp_.add_sub_('sub')
    elif word0 == 'neg':
        AsmStrOfFile += Comp_.neg_()
    elif word0 == 'eq':
        AsmStrOfFile += Comp_.eq_(labelCounter)
    elif word0 == 'gt':
        AsmStrOfFile += Comp_.gt_(labelCounter)
    elif word0 == 'lt':
        AsmStrOfFile += Comp_.lt_(labelCounter)
    elif word0 == 'and':
        AsmStrOfFile += Comp_.and_()
    elif word0 == 'or':
        AsmStrOfFile += Comp_.or_()
    elif word0 == 'not':
        AsmStrOfFile += Comp_.not_()
    elif word0 == 'label':
        AsmStrOfFile += Flow_.label_(word1,currentFunction)
    elif word0 == 'goto':
        AsmStrOfFile += Flow_.goto_(word1, currentFunction)
    elif word0 == 'if-goto':
        AsmStrOfFile += Flow_.if_goto_(word1, currentFunction)
    elif word0 == 'call':
        AsmStrOfFile += Flow_.call_(word1, word2, labelCounter)
    elif word0 == 'return':
        AsmStrOfFile += Flow_.return_()
    elif word0 == 'function':
        AsmStrOfFile += Flow_.function_(word1, word2)
    return AsmStrOfFile