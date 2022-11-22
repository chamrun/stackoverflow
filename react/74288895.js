const handleSubmit = async () => {
  await dispatch(myAction(...))
}

useEffect(() => {
  setIsPopupOpen(true)
}, [isPopupOpen])


// You do not need to `clearActionStatus()`, as long as `actionStatus` is not changed, the `useEffect` will not be triggered.