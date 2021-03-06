# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_mediatools_swig')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_mediatools_swig')
    _mediatools_swig = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_mediatools_swig', [dirname(__file__)])
        except ImportError:
            import _mediatools_swig
            return _mediatools_swig
        try:
            _mod = imp.load_module('_mediatools_swig', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _mediatools_swig = swig_import_helper()
    del swig_import_helper
else:
    import _mediatools_swig
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr



def high_res_timer_now():
    """high_res_timer_now() -> gr::high_res_timer_type"""
    return _mediatools_swig.high_res_timer_now()

def high_res_timer_now_perfmon():
    """high_res_timer_now_perfmon() -> gr::high_res_timer_type"""
    return _mediatools_swig.high_res_timer_now_perfmon()

def high_res_timer_tps():
    """high_res_timer_tps() -> gr::high_res_timer_type"""
    return _mediatools_swig.high_res_timer_tps()

def high_res_timer_epoch():
    """high_res_timer_epoch() -> gr::high_res_timer_type"""
    return _mediatools_swig.high_res_timer_epoch()
class mediatools_audiosource_s_sptr(object):
    """Proxy of C++ boost::shared_ptr<(mediatools_audiosource_s)> class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(boost::shared_ptr<(mediatools_audiosource_s)> self) -> mediatools_audiosource_s_sptr
        __init__(boost::shared_ptr<(mediatools_audiosource_s)> self, mediatools_audiosource_s * p) -> mediatools_audiosource_s_sptr
        """
        this = _mediatools_swig.new_mediatools_audiosource_s_sptr(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __deref__(self):
        """__deref__(mediatools_audiosource_s_sptr self) -> mediatools_audiosource_s *"""
        return _mediatools_swig.mediatools_audiosource_s_sptr___deref__(self)

    __swig_destroy__ = _mediatools_swig.delete_mediatools_audiosource_s_sptr
    __del__ = lambda self: None

    def enqueue(self, file):
        """enqueue(mediatools_audiosource_s_sptr self, std::string file)"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_enqueue(self, file)


    def skip(self):
        """skip(mediatools_audiosource_s_sptr self)"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_skip(self)


    def work(self, noutput_items, input_items, output_items):
        """work(mediatools_audiosource_s_sptr self, int noutput_items, gr_vector_const_void_star & input_items, gr_vector_void_star & output_items) -> int"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_work(self, noutput_items, input_items, output_items)


    def history(self):
        """history(mediatools_audiosource_s_sptr self) -> unsigned int"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_history(self)


    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(mediatools_audiosource_s_sptr self, int which, int delay)
        declare_sample_delay(mediatools_audiosource_s_sptr self, unsigned int delay)
        """
        return _mediatools_swig.mediatools_audiosource_s_sptr_declare_sample_delay(self, *args)


    def sample_delay(self, which):
        """sample_delay(mediatools_audiosource_s_sptr self, int which) -> unsigned int"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_sample_delay(self, which)


    def output_multiple(self):
        """output_multiple(mediatools_audiosource_s_sptr self) -> int"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_output_multiple(self)


    def relative_rate(self):
        """relative_rate(mediatools_audiosource_s_sptr self) -> double"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_relative_rate(self)


    def start(self):
        """start(mediatools_audiosource_s_sptr self) -> bool"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_start(self)


    def stop(self):
        """stop(mediatools_audiosource_s_sptr self) -> bool"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_stop(self)


    def nitems_read(self, which_input):
        """nitems_read(mediatools_audiosource_s_sptr self, unsigned int which_input) -> uint64_t"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_nitems_read(self, which_input)


    def nitems_written(self, which_output):
        """nitems_written(mediatools_audiosource_s_sptr self, unsigned int which_output) -> uint64_t"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_nitems_written(self, which_output)


    def max_noutput_items(self):
        """max_noutput_items(mediatools_audiosource_s_sptr self) -> int"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_max_noutput_items(self)


    def set_max_noutput_items(self, m):
        """set_max_noutput_items(mediatools_audiosource_s_sptr self, int m)"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_set_max_noutput_items(self, m)


    def unset_max_noutput_items(self):
        """unset_max_noutput_items(mediatools_audiosource_s_sptr self)"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_unset_max_noutput_items(self)


    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(mediatools_audiosource_s_sptr self) -> bool"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_is_set_max_noutput_items(self)


    def set_min_noutput_items(self, m):
        """set_min_noutput_items(mediatools_audiosource_s_sptr self, int m)"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_set_min_noutput_items(self, m)


    def min_noutput_items(self):
        """min_noutput_items(mediatools_audiosource_s_sptr self) -> int"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_min_noutput_items(self)


    def max_output_buffer(self, i):
        """max_output_buffer(mediatools_audiosource_s_sptr self, int i) -> long"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_max_output_buffer(self, i)


    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(mediatools_audiosource_s_sptr self, long max_output_buffer)
        set_max_output_buffer(mediatools_audiosource_s_sptr self, int port, long max_output_buffer)
        """
        return _mediatools_swig.mediatools_audiosource_s_sptr_set_max_output_buffer(self, *args)


    def min_output_buffer(self, i):
        """min_output_buffer(mediatools_audiosource_s_sptr self, int i) -> long"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_min_output_buffer(self, i)


    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(mediatools_audiosource_s_sptr self, long min_output_buffer)
        set_min_output_buffer(mediatools_audiosource_s_sptr self, int port, long min_output_buffer)
        """
        return _mediatools_swig.mediatools_audiosource_s_sptr_set_min_output_buffer(self, *args)


    def pc_noutput_items(self):
        """pc_noutput_items(mediatools_audiosource_s_sptr self) -> float"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_noutput_items(self)


    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(mediatools_audiosource_s_sptr self) -> float"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_noutput_items_avg(self)


    def pc_noutput_items_var(self):
        """pc_noutput_items_var(mediatools_audiosource_s_sptr self) -> float"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_noutput_items_var(self)


    def pc_nproduced(self):
        """pc_nproduced(mediatools_audiosource_s_sptr self) -> float"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_nproduced(self)


    def pc_nproduced_avg(self):
        """pc_nproduced_avg(mediatools_audiosource_s_sptr self) -> float"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_nproduced_avg(self)


    def pc_nproduced_var(self):
        """pc_nproduced_var(mediatools_audiosource_s_sptr self) -> float"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_nproduced_var(self)


    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(mediatools_audiosource_s_sptr self, int which) -> float
        pc_input_buffers_full(mediatools_audiosource_s_sptr self) -> pmt_vector_float
        """
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_input_buffers_full(self, *args)


    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(mediatools_audiosource_s_sptr self, int which) -> float
        pc_input_buffers_full_avg(mediatools_audiosource_s_sptr self) -> pmt_vector_float
        """
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_input_buffers_full_avg(self, *args)


    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(mediatools_audiosource_s_sptr self, int which) -> float
        pc_input_buffers_full_var(mediatools_audiosource_s_sptr self) -> pmt_vector_float
        """
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_input_buffers_full_var(self, *args)


    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(mediatools_audiosource_s_sptr self, int which) -> float
        pc_output_buffers_full(mediatools_audiosource_s_sptr self) -> pmt_vector_float
        """
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_output_buffers_full(self, *args)


    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(mediatools_audiosource_s_sptr self, int which) -> float
        pc_output_buffers_full_avg(mediatools_audiosource_s_sptr self) -> pmt_vector_float
        """
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_output_buffers_full_avg(self, *args)


    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(mediatools_audiosource_s_sptr self, int which) -> float
        pc_output_buffers_full_var(mediatools_audiosource_s_sptr self) -> pmt_vector_float
        """
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_output_buffers_full_var(self, *args)


    def pc_work_time(self):
        """pc_work_time(mediatools_audiosource_s_sptr self) -> float"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_work_time(self)


    def pc_work_time_avg(self):
        """pc_work_time_avg(mediatools_audiosource_s_sptr self) -> float"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_work_time_avg(self)


    def pc_work_time_var(self):
        """pc_work_time_var(mediatools_audiosource_s_sptr self) -> float"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_work_time_var(self)


    def pc_work_time_total(self):
        """pc_work_time_total(mediatools_audiosource_s_sptr self) -> float"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_work_time_total(self)


    def pc_throughput_avg(self):
        """pc_throughput_avg(mediatools_audiosource_s_sptr self) -> float"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_pc_throughput_avg(self)


    def set_processor_affinity(self, mask):
        """set_processor_affinity(mediatools_audiosource_s_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_set_processor_affinity(self, mask)


    def unset_processor_affinity(self):
        """unset_processor_affinity(mediatools_audiosource_s_sptr self)"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_unset_processor_affinity(self)


    def processor_affinity(self):
        """processor_affinity(mediatools_audiosource_s_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_processor_affinity(self)


    def active_thread_priority(self):
        """active_thread_priority(mediatools_audiosource_s_sptr self) -> int"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_active_thread_priority(self)


    def thread_priority(self):
        """thread_priority(mediatools_audiosource_s_sptr self) -> int"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_thread_priority(self)


    def set_thread_priority(self, priority):
        """set_thread_priority(mediatools_audiosource_s_sptr self, int priority) -> int"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_set_thread_priority(self, priority)


    def name(self):
        """name(mediatools_audiosource_s_sptr self) -> std::string"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_name(self)


    def symbol_name(self):
        """symbol_name(mediatools_audiosource_s_sptr self) -> std::string"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_symbol_name(self)


    def input_signature(self):
        """input_signature(mediatools_audiosource_s_sptr self) -> io_signature_sptr"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_input_signature(self)


    def output_signature(self):
        """output_signature(mediatools_audiosource_s_sptr self) -> io_signature_sptr"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_output_signature(self)


    def unique_id(self):
        """unique_id(mediatools_audiosource_s_sptr self) -> long"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_unique_id(self)


    def to_basic_block(self):
        """to_basic_block(mediatools_audiosource_s_sptr self) -> basic_block_sptr"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_to_basic_block(self)


    def check_topology(self, ninputs, noutputs):
        """check_topology(mediatools_audiosource_s_sptr self, int ninputs, int noutputs) -> bool"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_check_topology(self, ninputs, noutputs)


    def alias(self):
        """alias(mediatools_audiosource_s_sptr self) -> std::string"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_alias(self)


    def set_block_alias(self, name):
        """set_block_alias(mediatools_audiosource_s_sptr self, std::string name)"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_set_block_alias(self, name)


    def _post(self, which_port, msg):
        """_post(mediatools_audiosource_s_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _mediatools_swig.mediatools_audiosource_s_sptr__post(self, which_port, msg)


    def message_ports_in(self):
        """message_ports_in(mediatools_audiosource_s_sptr self) -> swig_int_ptr"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_message_ports_in(self)


    def message_ports_out(self):
        """message_ports_out(mediatools_audiosource_s_sptr self) -> swig_int_ptr"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_message_ports_out(self)


    def message_subscribers(self, which_port):
        """message_subscribers(mediatools_audiosource_s_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _mediatools_swig.mediatools_audiosource_s_sptr_message_subscribers(self, which_port)

mediatools_audiosource_s_sptr_swigregister = _mediatools_swig.mediatools_audiosource_s_sptr_swigregister
mediatools_audiosource_s_sptr_swigregister(mediatools_audiosource_s_sptr)


mediatools_audiosource_s_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id ())


def audiosource_s(args):
    """audiosource_s(std::vector< std::string,std::allocator< std::string > > args) -> mediatools_audiosource_s_sptr"""
    return _mediatools_swig.audiosource_s(args)


