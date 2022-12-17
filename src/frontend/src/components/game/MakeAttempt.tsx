import React, { useState } from 'react'

import { useAppDispatch } from '../../hooks/app'
import { attemptOperations } from '../../store/attempt/operations'

export const MakeAttempt: React.FC = () => {
	const dispatch = useAppDispatch()
	const [word, setWord] = useState<string>('')

	const attemptHandler = () => {
		dispatch(attemptOperations.make({ attempt: word }))
	}

	return (
		<div>
			<input type='text' onChange={(e) => setWord(e.target.value)} />
			<button onClick={attemptHandler}>Отправить</button>
		</div>
	)
}
