#define RET_BASE                                1

#define RET_SUCCESS                             (RET_BASE << 0)  ///< Successful command
#define RET_ERROR_UNDEFINE                      (RET_BASE << 1)  ///< Un-define error
#define RET_ERROR_NO_MEM                        (RET_BASE << 2)  ///< No Memory for operation
#define RET_ERROR_NOT_FOUND                     (RET_BASE << 3)  ///< Not found
#define RET_ERROR_NOT_SUPPORTED                 (RET_BASE << 4)  ///< Not supported
#define RET_ERROR_INVALID_PARAM                 (RET_BASE << 5)  ///< Invalid Parameter
#define RET_ERROR_INVALID_STATE                 (RET_BASE << 6)  ///< Invalid state, operation disallowed in this state
#define RET_ERROR_INVALID_LENGTH                (RET_BASE << 7)  ///< Invalid Length
#define RET_ERROR_INVALID_FLAGS                 (RET_BASE << 8)  ///< Invalid Flags
#define RET_ERROR_INVALID_DATA                  (RET_BASE << 9)  ///< Invalid Data
#define RET_ERROR_DATA_SIZE                     (RET_BASE << 10) ///< Invalid Data size
#define RET_ERROR_TIMEOUT                       (RET_BASE << 11) ///< Operation timed out
#define RET_ERROR_NULL                          (RET_BASE << 12) ///< Null Pointer
#define RET_ERROR_FORBIDDEN                     (RET_BASE << 13) ///< Forbidden Operation
#define RET_ERROR_INVALID_ADDR                  (RET_BASE << 14) ///< Bad Memory Address
#define RET_ERROR_BUSY                          (RET_BASE << 15) ///< Busy
#define RET_ERROR_OVER_MAX_NUM                  (RET_BASE << 16) ///< Over max num
#define RET_ERROR_PLATFORM                      (RET_BASE << 17) ///< Platform error
#define RET_ERROR_FULL                          (RET_BASE << 18) ///< Pool full
#define RET_ERROR_ALREADY_EXIST                 (RET_BASE << 19) ///< Already exist
#define RET_ERROR_TRANSMISSION_FAIL             (RET_BASE << 20) ///< Transmission fail
#define RET_ERROR_EMPTY                         (RET_BASE << 21)